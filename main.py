from fastapi import FastAPI
from mysite.api import user_profile,category,subcategory,product,review,cart,cart_item,favorite_item,favorite,auth

from mysite.admin.setup import setup_admin



wildberies_app = FastAPI(title='Wildberies-AI25')
wildberies_app.include_router(user_profile.user_router)
wildberies_app.include_router(category.category_router)
wildberies_app.include_router(subcategory.subcategory_router)
wildberies_app.include_router(product.product_router)
wildberies_app.include_router(review.review_router)
wildberies_app.include_router(cart.cart_router)
wildberies_app.include_router(cart_item.cart_item_router)
wildberies_app.include_router(favorite.favorite_router)
wildberies_app.include_router(favorite_item.favorite_item_router)
wildberies_app.include_router(auth.auth_router)

setup_admin(wildberies_app)
