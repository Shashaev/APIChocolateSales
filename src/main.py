import fastapi
import pandas as pd
import pydantic
import uvicorn

import pipeline


class ChocolateInformation(pydantic.BaseModel):
    sales_person: str = pydantic.Field(
        min_length=1,
        description='The name of the salesperson responsible for the sale.',
        examples=[
            'Jehu Rudeforth',
            'Van Tuxwell',
            'Gigi Bohling',
            'Jan Morforth',
        ],
        strict=True,
    )
    country: str = pydantic.Field(
        min_length=1,
        description='The country where the sale was made.',
        examples=[
            'Canada',
            'India',
            'Australia',
            'USA',
        ],
        strict=True,
    )
    product: str = pydantic.Field(
        min_length=1,
        description='The name and type of the product sold.',
        examples=[
            'Mint Chip Choco',
            '85% Dark Bars',
            'Peanut Butter Cubes',
            'Spicy Special Slims',
        ],
        strict=True,
    )
    boxes_shipped: int = pydantic.Field(
        ge=1,
        description=(
            'The number of product boxes shipped '
            'as part of the transaction.'
        ),
    )


app = fastapi.FastAPI()


@app.post('/delivery_price_chocolate')
def get_delivery_price(choc_info: ChocolateInformation) -> float:
    data = pd.DataFrame({
        'Sales Person': [choc_info.sales_person],
        'Country': [choc_info.country],
        'Product': [choc_info.product],
        'Boxes Shipped': [choc_info.boxes_shipped],
    })
    return pipeline.get_prediction(data)


if __name__ == '__main__':
    uvicorn.run(app, port=9876)
