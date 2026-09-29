# Online ordering wait-time engine pattern

Use when rebuilding or briefing a restaurant ordering page, takeaway checkout, pickup/delivery flow, or POS-adjacent food-ordering prototype.

## Core lesson

Do not frame the rebuild as just a menu clone. The strategic product is the wait-time and capacity engine behind the menu. The visual menu is easy; customer trust depends on accurate, adjustable pickup times.

## Observed reference pattern

A HungryHungry ordering page may show:
- Store status such as `Currently available for PreOrder`
- Pickup hours such as `4:30pm-7:45pm`
- Ordering modal such as `First Available: 4:45pm`
- This implies `first available = opening time + minimum lead time`, often 15 minutes

## Required logic inputs

- Opening hours and closed days
- Minimum prep time
- Pickup slot interval, e.g. five, 10, or 15 minutes
- Maximum orders per slot
- Menu item prep class, e.g. pizza, schnitzel, sides, drinks
- Current kitchen load from active orders
- Manual delay set by staff
- Last-order cut-off before close
- Sold-out status by item

## First available time formula

```text
first available time =
current time or next opening time
+ base prep time
+ item complexity delay
+ kitchen load delay
+ manual delay
rounded up to next valid slot
```

## Rule set

1. If the shop is closed but opens later today, show preorder and use `opening time + minimum prep time`.
2. If the shop is open and quiet, use `now + base prep time` rounded to the next slot.
3. If the kitchen is busy, add a queue delay based on active orders and slot capacity.
4. If the preferred slot is full, push to the next available slot.
5. If the calculated time breaches the last-order cut-off, block ordering or push to the next valid trading day.

## Admin controls are mandatory

A restaurant wait-time rebuild needs staff override controls from the MVP, not later. Include:
- Pause orders
- Add 10, 15, 30, or 45 minutes
- Mark item sold out
- Close early today
- Reopen ordering

## MVP build scope

Start lean:
1. Menu page
2. Cart
3. First available pickup time
4. Select another time
5. Admin delay controls
6. Order submission to email, SMS, or kitchen dashboard
7. Fake payment first, Stripe later unless the user explicitly asks for live checkout

## Pitfall

Do not lead with POS integration. It increases complexity before the workflow is proven. Prototype the ordering and wait-time trust loop first, then wire payments and integrations.