 
from uagents import Agent, Bureau, Context, Model


interval=3.0
rate=0.1288

class Request(Model):
    request: float
    house: str
class Message(Model):
    message: str
    request: float
    house: str

house1 = Agent(name="house1", seed="ANTNhousehold1", port=8000, endpoint=["http://localhost:8000/submit"])
house2 = Agent(name="house2", seed="ANTNhousehold2", port=8001, endpoint=["http://localhost:8001/submit"])
house3 = Agent(name="house3", seed="ANTNhousehold3", port=8002, endpoint=["http://localhost:8002/submit"])
house4 = Agent(name="house4", seed="ANTNhousehold4", port=8003, endpoint=["http://localhost:8003/submit"])

house1.stored_data = {"bank": 100.0, "production": 30.0, "usage": 10.0, "money":0.0, "mult":4.0}
house2.stored_data = {"bank": 100.0, "production": 60.0, "usage": 10.0, "money":0.0, "mult":1.0}
house3.stored_data = {"bank": 100.0, "production": 30.0, "usage": 10.0, "money":0.0, "mult":5.0}
house4.stored_data = {"bank": 100.0, "production": 30.0, "usage": 10.0, "money":0.0, "mult":3.5}

address_book = {"house1": house1.address, "house2": house2.address, "house3": house3.address, "house4": house4.address}

#house 1

@house1.on_interval(period=interval)
async def house1_update(ctx: Context):
    ctx.logger.info(f"{house1.stored_data}")
    house1.stored_data["bank"] += house1.stored_data["production"] - house1.stored_data["usage"]*house1.stored_data["mult"]
    #check if need to buy
    if house1.stored_data["production"]<house1.stored_data["usage"]*house1.stored_data["mult"] and house1.stored_data["bank"] <= 2 * house1.stored_data["usage"]*house1.stored_data["mult"]:
        #send buy messages
        request_amt=house1.stored_data["usage"]*house1.stored_data["mult"]*5-house1.stored_data["bank"]
        await ctx.send(house2.address, Request(request=request_amt, house="house1"))

@house1.on_message(model=Message)
async def house1_message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    if msg.message=="Filled!":
        house1.stored_data["bank"]+=msg.request
        house1.stored_data["money"]-=msg.request*rate
    else:
        if msg.house=="house2":
            await ctx.send(house3.address, Request(request=msg.request, house="house1"))
        elif msg.house=="house3":
            await ctx.send(house4.address, Request(request=msg.request, house="house1"))

#receive buy order
@house1.on_message(model=Request)
async def house1_req_handler(ctx: Context, sender: str, msg: Request):
    ctx.logger.info(f"Received request from {sender}: {msg.request} kWh")
    available=house1.stored_data["bank"]-house1.stored_data["usage"]*house1.stored_data["mult"]*5
    if msg.request<=available:
        house1.stored_data["bank"]-=msg.request
        house1.stored_data["money"]+=msg.request*rate
        await ctx.send(address_book[msg.house], Message(message="Filled!", request=msg.request, house="house1"))
    else:
        await ctx.send(address_book[msg.house], Message(message="Not enough resources!", request=msg.request, house="house1"))        
        



#house 2
@house2.on_interval(period=interval)
async def house2_update(ctx: Context):
    ctx.logger.info(f"{house2.stored_data}")
    house2.stored_data["bank"] += house2.stored_data["production"] - house2.stored_data["usage"]*house2.stored_data["mult"]
    #check if need to buy
    if house2.stored_data["production"]<house2.stored_data["usage"]*house2.stored_data["mult"] and house2.stored_data["bank"] <= 2 * house2.stored_data["usage"]*house2.stored_data["mult"]:
        #send buy messages
        request_amt=house2.stored_data["usage"]*house2.stored_data["mult"]*5-house2.stored_data["bank"]
        await ctx.send(house3.address, Request(request=request_amt, house="house2"))
#receive order feedback message
@house2.on_message(model=Message)
async def house2_message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    if msg.message=="Filled!":
        house2.stored_data["bank"]+=msg.request
        house2.stored_data["money"]-=msg.request*rate
    else:
        if msg.house=="house3":
            await ctx.send(house4.address, Request(request=msg.request, house="house2"))
        elif msg.house=="house4":
            await ctx.send(house1.address, Request(request=msg.request, house="house2"))

#receive buy order
@house2.on_message(model=Request)
async def house2_req_handler(ctx: Context, sender: str, msg: Request):
    ctx.logger.info(f"Received request from {sender}: {msg.request} kWh")
    available=house2.stored_data["bank"]-house2.stored_data["usage"]*house2.stored_data["mult"]*5
    if msg.request<=available:
        house2.stored_data["bank"]-=msg.request
        house2.stored_data["money"]+=msg.request*rate
        await ctx.send(address_book[msg.house], Message(message="Filled!", request=msg.request, house="house2"))
    else:
        await ctx.send(address_book[msg.house], Message(message="Not enough resources!", request=msg.request, house="house2"))

#house 3
@house3.on_interval(period=interval)
async def house3_update(ctx: Context):
    ctx.logger.info(f"{house3.stored_data}")
    house3.stored_data["bank"] += house3.stored_data["production"] - house3.stored_data["usage"]*house3.stored_data["mult"]
    #check if need to buy
    if house3.stored_data["production"]<house3.stored_data["usage"]*house3.stored_data["mult"] and house3.stored_data["bank"] <= 2 * house3.stored_data["usage"]*house3.stored_data["mult"]:
        #send buy messages
        request_amt=house3.stored_data["usage"]*house3.stored_data["mult"]*5-house3.stored_data["bank"]
        await ctx.send(house4.address, Request(request=request_amt, house="house3"))
#receive order feedback message
@house3.on_message(model=Message)
async def house3_message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    if msg.message=="Filled!":
        house3.stored_data["bank"]+=msg.request
        house3.stored_data["money"]-=msg.request*rate
    else:
        if msg.house=="house1":
            await ctx.send(house2.address, Request(request=msg.request, house="house3"))
        elif msg.house=="house4":
            await ctx.send(house1.address, Request(request=msg.request, house="house3"))
            
#receive buy order
@house3.on_message(model=Request)
async def house3_req_handler(ctx: Context, sender: str, msg: Request):
    ctx.logger.info(f"Received request from {sender}: {msg.request} kWh")
    available=house3.stored_data["bank"]-house3.stored_data["usage"]*house3.stored_data["mult"]*5
    if msg.request<=available:
        house3.stored_data["bank"]-=msg.request
        house3.stored_data["money"]+=msg.request*rate
        await ctx.send(address_book[msg.house], Message(message="Filled!", request=msg.request, house="house3"))
    else:
        await ctx.send(address_book[msg.house], Message(message="Not enough resources!", request=msg.request, house="house3"))

#house 4
@house4.on_interval(period=interval)
async def house4_update(ctx: Context):
    ctx.logger.info(f"{house4.stored_data}")
    house4.stored_data["bank"] += house4.stored_data["production"] - house4.stored_data["usage"]*house4.stored_data["mult"]
    #check if need to buy
    if house4.stored_data["production"]<house4.stored_data["usage"]*house4.stored_data["mult"] and house4.stored_data["bank"] <= 2 * house4.stored_data["usage"]*house4.stored_data["mult"]:
        #send buy messages
        request_amt=house4.stored_data["usage"]*house4.stored_data["mult"]*5-house4.stored_data["bank"]
        await ctx.send(house1.address, Request(request=request_amt, house="house4"))
#receive order feedback message
@house4.on_message(model=Message)
async def house4_message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    if msg.message=="Filled!":
        house4.stored_data["bank"]+=msg.request
        house4.stored_data["money"]-=msg.request*rate
    else:
        if msg.house=="house1":
            await ctx.send(house2.address, Request(request=msg.request, house="house4"))
        elif msg.house=="house2":
            await ctx.send(house3.address, Request(request=msg.request, house="house4"))

            
#receive buy order
@house4.on_message(model=Request)
async def house4_req_handler(ctx: Context, sender: str, msg: Request):
    ctx.logger.info(f"Received request from {sender}: {msg.request} kWh")
    available=house4.stored_data["bank"]-house4.stored_data["usage"]*house4.stored_data["mult"]*5
    if msg.request<=available:
        house4.stored_data["bank"]-=msg.request
        house4.stored_data["money"]+=msg.request*rate
        await ctx.send(address_book[msg.house], Message(message="Filled!", request=msg.request, house="house4"))
    else:
        await ctx.send(address_book[msg.house], Message(message="Not enough resources!", request=msg.request, house="house4"))


bureau = Bureau()
bureau.add(house1)
bureau.add(house2)
bureau.add(house3)
bureau.add(house4)

if __name__ =="__main__":
    bureau.run()
