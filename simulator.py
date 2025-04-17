import asyncio

from pymodbus.server.simulator.http_server import ModbusSimulatorServer

async def run_server():
	simulator = ModbusSimulatorServer()
	await simulator.run_forever()

if __name__ == "__main__":
	asyncio.run(run_server())