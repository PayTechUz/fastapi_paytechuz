from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Request

from app import config
from app.models import Invoice
from app.dependencies import get_db
from app.webhook_handlers import CustomClickWebhookHandler, CustomPaymeWebhookHandler


router = APIRouter(
    prefix="/api/v1/webhooks",
    tags=["webhooks"]
)


@router.post("/payme")
async def payme_webhook(request: Request, db: Session = Depends(get_db)):
    handler = CustomPaymeWebhookHandler(
        db=db,
        payme_id=config.PAYME_ID,
        payme_key=config.PAYME_KEY,
        account_model=Invoice,
        account_field='id',
        amount_field='amount'
    )
    return await handler.handle_webhook(request)


@router.post("/click")
async def click_webhook(request: Request, db: Session = Depends(get_db)):
    handler = CustomClickWebhookHandler(
        db=db,
        service_id=config.CLICK_SERVICE_ID,
        secret_key=config.CLICK_SECRET_KEY,
        account_model=Invoice
    )
    return await handler.handle_webhook(request)
