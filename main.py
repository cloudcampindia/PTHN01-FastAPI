from fastapi import FastAPI

app = FastAPI(
    title="ECommerce API",
    description="An API for managing Orders placed by customers",
    docs_url='/'
)