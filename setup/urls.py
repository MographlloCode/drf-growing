from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from cells.views import CellViewset
from plants.views import PlantsViewset
from cultivator.views import CultivatorViewset, ListCultivatorData

router = routers.DefaultRouter()
router.register('cultivators', CultivatorViewset, basename='Cultivators')
router.register('cells', CellViewset, basename='Cells')
router.register('plants', PlantsViewset, basename='Plants')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # -- Cell routs
    # path('cell/<int:pk>/', ListCultivatorData.as_view()),
    # path('cell/<int:pk>/cultivators', ListCultivatorPlants.as_view()),
    # path('cell/<int:pk>/plants', ListCultivatorPlantData.as_view()),
    # -- Cultivator Routes
    path('cultivator/<int:pk>/', ListCultivatorData.as_view()),
    # path('cultivator/<int:pk>/plants', ListCultivatorPlants.as_view()),
    # path('cultivator/<int:pk>/plants/<int:pk>', ListCultivatorPlantData.as_view()),
    # path('cultivator/<int:pk>/cells', ListCultivatorCells.as_view()),
    # path('cultivator/<int:pk>/cells/<int:pk>', ListCultivatorCellData.as_view()),
    # -- Plant Routes
    # path('plant/<int:pk>/', ListCultivatorData.as_view()),
    # path('plant/<int:pk>/cells', ListCultivatorPlants.as_view()),
]
