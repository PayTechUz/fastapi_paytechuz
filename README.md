# Payment Integration Example

Modern FastAPI REST API for payment processing with Payme and Click, built on
[PayTechUZ](https://github.com/PayTechUz/paytechuz).

> **No license key.** PayTechUZ is MIT-licensed and fully open source since
> `0.4.0`. There is no `PAYTECH_LICENSE_API_KEY`, no activation and no usage
> limit — you only need your gateway credentials from Payme and Click.

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Copy `.env.example` to `.env` and update with your credentials:

```bash
cp .env.example .env
```

### 3. Run Application

```bash
./run.sh
# or
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

### Orders

**Create Order with Payment**

```http
POST /api/v1/orders
Content-Type: application/json

{
    "product_name": "Test Product",
    "amount": 100.00,
    "payment_method": "payme"
}
```

**Response:**
```json
{
    "id": 1,
    "amount": 100.00,
    "payment_method": "payme",
    "payment_link": "https://test.paycom.uz/..."
}
```

**Fields:**
- `id` - Order ID
- `amount` - Payment amount
- `payment_method` - Gateway name (payme, click)
- `payment_link` - Payment URL to redirect user

### Webhooks

- `POST /api/v1/webhooks/payme` - Payme webhook
- `POST /api/v1/webhooks/click` - Click webhook

## cURL Examples

**Payme Payment:**
```bash
curl -X POST http://127.0.0.1:8000/api/v1/orders \
  -H "Content-Type: application/json" \
  -d '{
    "product_name": "Premium Subscription",
    "amount": 50000.00,
    "payment_method": "payme"
  }'
```

**Response:**
```json
{
    "id": 1,
    "amount": 50000.00,
    "payment_method": "payme",
    "payment_link": "https://test.paycom.uz/..."
}
```

**Click Payment:**
```bash
curl -X POST http://127.0.0.1:8000/api/v1/orders \
  -H "Content-Type: application/json" \
  -d '{
    "product_name": "Monthly Plan",
    "amount": 25000.00,
    "payment_method": "click"
  }'
```

**Response:**
```json
{
    "id": 2,
    "amount": 25000.00,
    "payment_method": "click",
    "payment_link": "https://my.click.uz/services/pay?..."
}
```

## Testing Webhooks Locally

Use `jprq` or `ngrok` to expose your local server:

```bash
# Using jprq
jprq http 8000

# Using ngrok
ngrok http 8000
```

Configure webhook URLs in payment gateway admin panels:
- Payme: `https://your-domain.com/api/v1/webhooks/payme`
- Click: `https://your-domain.com/api/v1/webhooks/click`

## Resources

- [PayTechUZ Documentation](https://pay-tech.uz)
- [PayTechUZ on GitHub](https://github.com/PayTechUz/paytechuz)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Payme Documentation](https://developer.help.paycom.uz/)
- [Click Documentation](https://docs.click.uz/)
