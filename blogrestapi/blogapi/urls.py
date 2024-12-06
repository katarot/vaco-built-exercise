from django.urls import include, path
from .views import BlogPostCreate, BlogPostList, BlogPostDetail, BlogPostUpdate, BlogPostDelete, CategoryCreate, CategoryList, CategoryDetail, CategoryUpdate, CategoryDelete

urlpatterns = [

    # BLOG POST
    # <localhost>/blogpost/create/
    path('create/', BlogPostCreate.as_view(), name='create-blogpost'),              # POST          

    # <localhost>/blogpost/
    path('', BlogPostList.as_view()),                                               # GET           

    # <localhost>/blogpost/:id
    path('<int:pk>/', BlogPostDetail.as_view(), name='retrieve-blogpost'),          # GET/id        
    
    # <localhost>/blogpost/update/:id
    path('update/<int:pk>/', BlogPostUpdate.as_view(), name='update-blogpost'),     # PUT/id       

    # <localhost>/blogpost/delete/:id
    path('delete/<int:pk>/', BlogPostDelete.as_view(), name='delete-blogpost'),     # DELETE/id    
    

    # CATEGORY
    # <localhost>/blogpost/category/create/
    path('category/create/', CategoryCreate.as_view(), name='create-category'),          # POST   

    # <localhost>/blogpost/category/
    path('category/', CategoryList.as_view()),                                           # GET           

    # <localhost>/blogpost/category/:id
    path('category/<int:pk>/', CategoryDetail.as_view(), name='retrieve-category'),      # GET/id        
    
    # <localhost>/blogpost/category/update/:id
    path('category/update/<int:pk>/', CategoryUpdate.as_view(), name='update-category'),  # PUT/id        

    # <localhost>/blogpost/category/delete/:id
    path('category/delete/<int:pk>/', CategoryDelete.as_view(), name='delete-category') # DELETE/id     
]
