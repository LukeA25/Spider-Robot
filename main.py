import asyncio
from bleak import BleakClient
from bleak import BleakScanner
import keyboard

write_characteristic = "0000FFE1-0000-1000-8000-00805f9b34fb"


async def find():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)


async def main(address):
    loop = asyncio.get_event_loop()

    async with BleakClient(address) as client:
        svcs = await client.get_services()
        print("Services:")
        for service in svcs:
            print(service)
        while True:
            if client.is_connected:
                input_key = ""

                if keyboard.is_pressed("W"):
                    input_key = "W"
                if keyboard.is_pressed("A"):
                    input_key = "A"
                if keyboard.is_pressed("D"):
                    input_key = "D"
                if keyboard.is_pressed("S"):
                    input_key = "S"
                if keyboard.is_pressed("V"):
                    input_key = "V"
                if keyboard.is_pressed("B"):
                    input_key = "B"
                if input_key != "":
                    bytes_to_send = bytearray(map(ord, input_key))
                    await client.write_gatt_char(write_characteristic, bytes_to_send)
                    print(f"Sent: {input_key}")
                    await asyncio.sleep(1.3, loop=loop)
            else:
                await asyncio.sleep(2.0, loop=loop)


asyncio.run(main("4B6E98EC-20C9-B0BD-6684-FA86FF393A86"))
