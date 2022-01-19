from pypresence import Presence
import time, psutil

client_id = "933214976817119263"
rpc = Presence(client_id=client_id, pipe=0)
rpc.connect()
start_time = time.time()

while True:
    mem = psutil.virtual_memory()
    rpc.update(
        # buttons=[{"label": "Watchdog", "url": "https://petcafe.xyz/invite"}, {"label": "Server", "url": "https://discord.gg/jVc3ByWVd3"}], 
        large_image="intel_pentium_2020_logo", large_text="Intel Pentium G3250T @ 2.80GHz",
        small_image="microsoft-windows-server", small_text="Windows Server 2022 Datacenter", 
        start=start_time, 
        
        details=f"CPU ㅣ{round(psutil.cpu_percent(), 1)}% {round(psutil.cpu_freq().current/1024, 2)}GHz", 
        state=f"RAMㅣ{round(mem.percent, 1)}% {round(mem.used/1024**3, 1)}GB/{round(mem.total/1024**3, 1)}GB",
    )
    time.sleep(1)