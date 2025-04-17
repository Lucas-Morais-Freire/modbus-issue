import sys
from pymodbus.client import AsyncModbusTcpClient
import asyncio

async def run_client():
    client = AsyncModbusTcpClient("127.0.0.1", port=5020)

    await client.connect()
    assert client.connected
    print("connected!")


    pdu = await client.read_holding_registers(int(sys.argv[1]))
    print(f'returned function code: {hex(pdu.function_code)}.')

    # pdu = await client.read_holding_registers(10)
    # print(f'returned function code: {hex(pdu.function_code)}.')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Pass the address of the register you want to read.")
        quit(-1)
    asyncio.run(run_client(), debug=True)