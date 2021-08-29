from controller.users import Users
from fastapi import APIRouter
from libs.phrase import generate
from pydantic import BaseModel

router = APIRouter()


class MacAddress(BaseModel):
    mac_address: str


@router.post("/hard/sendphrase")
async def send_string(mac_address: MacAddress):
    mac_addr = mac_address.mac_address
    stopFlag = Users().is_sending(mac_addr)
    print(stopFlag)
    phrase = generate()
    Users().set_phrase_and_score(mac_addr, phrase)

    # 1か0を付与する
    return {"phrase": str(int(stopFlag))+phrase}
