import psutil
import platform
import GPUtil
from datetime import datetime
from tkinter import *
import webbrowser

root = Tk()
root.title('System and Hardware Info @_python.py_')
root.geometry('680x400')
root.resizable(False, False)
root.config(bg='#00154f')

Label(root, text='System and Hardware Information', font='Verdana 20 bold', fg='#f2bc94', bg="#00154f").pack()
Label(root, text='@_python.py_', font='Verdana 13 bold', fg='#f4af1b', bg="#00154f").pack()
TextBox = Text(root, height=15, width=57, font='Verdana 10 bold')
TextBox.place(x = 140, y= 150)


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def SystemInfo():
    TextBox.delete('1.0', END)
    TextBox.insert(END, '______________System Information______________\n\n')
    uname = platform.uname()
    TextBox.insert(END, f"System: {uname.system}\n")
    TextBox.insert(END, f"Node Name: {uname.node}\n")
    TextBox.insert(END, f"Release: {uname.release}\n")
    TextBox.insert(END, f"Version: {uname.version}\n")
    TextBox.insert(END, f"Machine: {uname.machine}\n")
    TextBox.insert(END, f"Processor: {uname.processor}")

# Boot Time
def boottime():
    TextBox.delete('1.0', END)
    TextBox.insert(END, '______________BOOT TIME______________\n\n')
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    TextBox.insert(END, f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

# let's print CPU information
def CPUInfo():
    TextBox.delete('1.0', END)
    TextBox.insert(END, '______________CPU INFORMATION______________\n\n')
    # number of cores
    TextBox.insert(END, f"Physical cores: {psutil.cpu_count(logical=False)}\n")
    TextBox.insert(END, f"Total cores: {psutil.cpu_count(logical=True)}\n")
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    TextBox.insert(END, f"Max Frequency: {cpufreq.max:.2f}Mhz \n")
    TextBox.insert(END, f"Min Frequency: {cpufreq.min:.2f}Mhz \n")
    TextBox.insert(END, f"Current Frequency: {cpufreq.current:.2f}Mhz \n")
    # CPU usage
    TextBox.insert(END, "CPU Usage Per Core: \n")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        TextBox.insert(END, f"Core {i}: {percentage}% \n")
    TextBox.insert(END, f"Total CPU Usage: {psutil.cpu_percent()}% \n\n")

    TextBox.insert(END, "___ BATTERY INFO ___ \n")
    info = list(psutil.sensors_battery())
    TextBox.insert(END, f" Percentage: {info[0]}\n")
    TextBox.insert(END, f" Plugged-in: {info[2]}")

# Memory Information
def MemoryInfo():
    TextBox.delete('1.0', END)
    TextBox.insert(END, '______________MEMORY(RAM) INFORMATION______________\n\n')
    # get the memory details
    svmem = psutil.virtual_memory()
    TextBox.insert(END, f"Total: {get_size(svmem.total)} \n")
    TextBox.insert(END, f"Available: {get_size(svmem.available)} \n")
    TextBox.insert(END, f"Used: {get_size(svmem.used)} \n")
    TextBox.insert(END, f"Percentage: {svmem.percent}% \n")

    # get the swap memory details (if exists)
    TextBox.insert(END, "______________SWAP MEMORY DETAILS (if exist)___________\n\n")
    swap = psutil.swap_memory()
    TextBox.insert(END, f"Total: {get_size(swap.total)} \n")
    TextBox.insert(END, f"Free: {get_size(swap.free)} \n")
    TextBox.insert(END, f"Used: {get_size(swap.used)} \n")
    TextBox.insert(END, f"Percentage: {swap.percent}% ")

# Disk Information
def DiskInfo():
    TextBox.delete('1.0', END)
    TextBox.insert(END, '______________DISK INFORMATION______________\n\n')
    TextBox.insert(END, "Partitions and Usage:\n")
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        TextBox.insert(END, f"=== Device: {partition.device} === \n")
        TextBox.insert(END, f"  Mountpoint: {partition.mountpoint} \n")
        TextBox.insert(END, f"  File system type: {partition.fstype} \n")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        TextBox.insert(END, f"  Total Size: {get_size(partition_usage.total)} \n")
        TextBox.insert(END, f"  Used: {get_size(partition_usage.used)} \n")
        TextBox.insert(END, f"  Free: {get_size(partition_usage.free)} \n")
        TextBox.insert(END, f"  Percentage: {partition_usage.percent}% \n\n")
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    TextBox.insert(END, f"Total read: {get_size(disk_io.read_bytes)} \n")
    TextBox.insert(END, f"Total write: {get_size(disk_io.write_bytes)} ")

# Network information
def NetworkInfo():
    TextBox.delete('1.0', END)
    TextBox.insert(END, '______________NETWORK INFORMATION______________\n\n')
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            TextBox.insert(END, f"=== Interface: {interface_name} === \n")
            if str(address.family) == 'AddressFamily.AF_INET':
                TextBox.insert(END, f"  IP Address: {address.address} \n")
                TextBox.insert(END, f"  Netmask: {address.netmask} \n")
                TextBox.insert(END, f"  Broadcast IP: {address.broadcast} \n")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                TextBox.insert(END, f"  MAC Address: {address.address} \n")
                TextBox.insert(END, f"  Netmask: {address.netmask} \n")
                TextBox.insert(END, f"  Broadcast MAC: {address.broadcast} \n")
    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    TextBox.insert(END, f"Total Bytes Sent: {get_size(net_io.bytes_sent)} \n")
    TextBox.insert(END, f"Total Bytes Received: {get_size(net_io.bytes_recv)} \n")

# GPU information
def GPUInfo():
    TextBox.delete('1.0', END)
    TextBox.insert(END, '______________GPU INFORMATION______________\n\n')
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        # get the GPU id
        TextBox.insert(END, f" GPU ID : {gpu.id} \n")
        # name of GPU
        TextBox.insert(END, f"GPU NAME :  {gpu.name} \n")
        # get % percentage of GPU usage of that GPU
        TextBox.insert(END, f"Load : {gpu.load*100}% \n")
        # get free memory in MB format
        TextBox.insert(END, f"Memory Free : {gpu.memoryFree}MB \n")
        # get used memory
        TextBox.insert(END, f"Memory Used : {gpu.memoryUsed}MB \n")
        # get total memory
        TextBox.insert(END, f"Memory Total : {gpu.memoryTotal}MB \n")
        # get GPU temperature in Celsius
        TextBox.insert(END, f"Temperature : {gpu.temperature} °C \n")
        TextBox.insert(END, f"vvid : {gpu.uuid}")

def Followme():
   webbrowser.open('https://www.instagram.com/_python.py_/')
Button(root, text='System Info', bg='#f2bc94', fg='#00154f', font='Verdana 10 bold', width=10, command=SystemInfo).place(x=20, y=100)
Button(root, text='Boot Time', bg='#f2bc94', fg='#00154f', font='Verdana 10 bold', width=10, command=boottime).place(x=140, y=100)
Button(root, text='CPU Info', bg='#f2bc94', fg='#00154f', font='Verdana 10 bold', width=10, command= CPUInfo).place(x=260, y=100)
Button(root, text='Memory Info', bg='#f2bc94', fg='#00154f', font='Verdana 10 bold', width=10, command=MemoryInfo).place(x=380, y=100)
Button(root, text='Disk Info', bg='#f2bc94', fg='#00154f', font='Verdana 10 bold', width=10, command=DiskInfo).place(x=500, y=100)
Button(root, text='Network Info', bg='#f2bc94', fg='#00154f', font='Verdana 10 bold', width=10, command = NetworkInfo).place(x=20, y=160)
Button(root, text='Graphic Info', bg='#f2bc94', fg='#00154f', font='Verdana 10 bold', width=10, command=GPUInfo).place(x=20, y=220)
Button(root, text='Follow', bg='#f2bc94', fg='#00154f', font='Verdana 10 bold', width=10, command=Followme).place(x=20, y=280)
Button(root, text='Exit', bg='#f2bc94', fg='#00154f', font='Verdana 10 bold', width=10, command=exit).place(x=20, y=340)


root.mainloop()
