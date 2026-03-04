from sqladmin import ModelView
from mysite.db.models import UserProfile,Category,SubCategory,Product,ImageProduct,Review,Favorite,FavoriteItem,Cart,CartItem,RefreshToken


class UserProfileView(ModelView, model=UserProfile):
    column_list = [UserProfile.id,UserProfile.username]

class RefreshTokenView(ModelView,model=RefreshToken):
    column_list = [RefreshToken.id,RefreshToken.user_id]

class CategoryView(ModelView, model=Category):
    column_list = [Category.id,Category.category_name]

class SubCategoryView(ModelView, model=SubCategory):
    column_list = [SubCategory.id,SubCategory.subcategory_name]

class ProductView(ModelView, model=Product):
    column_list = [Product.id,Product.product_name]

class ImageProductView(ModelView, model=ImageProduct):
    column_list = [ImageProduct.id,ImageProduct.image]

class ReviewView(ModelView, model=Review):
    column_list = [Review.id,Review.product_id]

class FavoriteView(ModelView, model=Favorite):
    column_list = [Favorite.id,Favorite.favorite_item]

class FavoriteItemView(ModelView, model=FavoriteItem):
    column_list = [FavoriteItem.id,FavoriteItem.product_id]

class CartView(ModelView, model=Cart):
    column_list = [Cart.id,Cart.cart_item]

class CartItemView(ModelView, model=CartItem):
    column_list = [CartItem.id,CartItem.product_id]
