import pexpect
import threading
import re, time

def scanble(hci="hci0", timeout=1):
    conn = pexpect.spawn("sudo hciconfig %s reset" % hci)
    time.sleep(0.2)

    conn = pexpect.spawn("sudo timeout %d hcitool lescan" % timeout)
    time.sleep(0.2)

    conn.expect("LE Scan \.+", timeout=timeout)
    output = ""
    adr_pat = "(?P<addr>([0-9A-F]{2}:){5}[0-9A-F]{2}) (?P<name>.*)"
    while True:
        try:
            res = conn.expect(adr_pat)
            s = conn.after.decode('utf-8')
            output += s + "\n"
        except pexpect.EOF:
            break

    lines = re.split('\r?\n', output.strip())
    lines = list(set(lines))
    lines = [line for line in lines if re.match(adr_pat, line)]
    lines = [re.match(adr_pat, line).groupdict() for line in lines]
    lines = [line for line in lines if re.match('.*', line['name'])]

    return lines

class BluetoothScan():
    isStoped = True

    #thread start
    def start(self, func, kind):
        if self.isStoped:
            t = threading.Thread(target=self.run, args=(func, kind))
            t.start()
        else:
            print("이미 쓰레드가 실행중입니다.")

    def run(self, func, kind):
        self.isStoped = False
        while True:
            if kind == 'ble':
                try:
                    print("BLE device scanning...")
                    conn = pexpect.spawn("sudo hciconfig hci0 reset")
                    time.sleep(0.2)
                    conn = pexpect.spawn("sudo timeout 5 hcitool lescan")
                    time.sleep(0.2)
                    conn.expect("LE Scan \.+")
                    adr_pat = "(?P<addr>([0-9A-F]{2}:){5}[0-9A-F]{2}) (?P<name>.*)"
                    output = ""
                except pexpect.EOF:
                    print("예외")
                    time.sleep(1)
                    continue

                while True:
                    try:
                        res = conn.expect(adr_pat)
                        bledevices = conn.after.decode('utf-8')
                        bledevices = bledevices.split(' ');
                        addr = bledevices[0]
                        name = bledevices[1].split('\r\n')[0]
                        func({'addr':addr,'name':name})
                    except pexpect.EOF:
                        break

            elif kind == 'classic':
                print("Bluetooth device scanning...")
                conn = pexpect.spawn("sudo timeout 5 hcitool scan")
                time.sleep(0.2)
                conn.expect("Scanning \.+")
                adr_pat = ".*(?P<addr>([0-9A-F]{2}:){5}[0-9A-F]{2}).*(?P<name>.*)"
                output = ""

                while True:
                    try:
                        res = conn.expect(adr_pat)
                        bledevices = conn.after.decode('utf-8')
                        bledevices = bledevices.split('\t');
                        addr = bledevices[1]
                        name = bledevices[2].split('\r\n')[0]
                        func({'addr':addr,'name':name})
                    except pexpect.EOF:
                        break
                time.sleep(5)

            if self.isStoped:
                break


    def stop(self):
        self.isStoped = True



scan = BluetoothScan()

#def showDvice(list):
#    print(list)

#scan.start(showDvice,'classic')
