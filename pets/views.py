from rest_framework.views import Request, Response, APIView, status
from .models import Pet
from .serializers import PetSerializer
from groups.models import Group
from traits.models import Trait
from rest_framework.pagination import PageNumberPagination


class PetView(APIView, PageNumberPagination):
    def post(self, req: Request) -> Response:
        serializer = PetSerializer(data=req.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        group_data = serializer.validated_data.pop("group")
        traits = serializer.validated_data.pop("traits")

        try:
            group = Group.objects.get(
                scientific_name__iexact=group_data["scientific_name"]
            )
        except Group.DoesNotExist:
            group = Group.objects.create(**group_data)

        pet = Pet.objects.create(**serializer.validated_data, group=group)

        trait_obj = []
        for trait_data in traits:
            try:
                trait = Trait.objects.get(name__iexact=trait_data["name"])
            except Trait.DoesNotExist:
                trait = Trait.objects.create(**trait_data)
            trait_obj.append(trait)
        pet.traits.set(trait_obj)

        serializer = PetSerializer(pet)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        by_trait = req.query_params.get("trait", None)
        if by_trait:
            pets = Pet.objects.filter(traits__name__icontains=by_trait)
        else:
            pets = Pet.objects.all()

        result = self.paginate_queryset(pets, req)
        serializer = PetSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)


class PetsDetailView(APIView):
    def get(self, req: Request, pet_id: int) -> Response:
        try:
            found_pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            return Response({"detail": "Not found."}, status.HTTP_404_NOT_FOUND)
        serializer = PetSerializer(found_pet)
        return Response(serializer.data)

    def delete(self, req: Request, pet_id: int) -> Response:
        try:
            found_pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            return Response({"detail": "Not found."}, status.HTTP_404_NOT_FOUND)
        found_pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, req: Request, pet_id: int) -> Response:
        try:
            found_pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            return Response({"detail": "Not found."}, status.HTTP_404_NOT_FOUND)
        serializer = PetSerializer(data=req.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        group_data = serializer.validated_data.pop("group", None)
        if group_data:
            try:
               group = Group.objects.get(scientific_name__iexact=group_data["scientific_name"])
            except Group.DoesNotExist:
                group = Group.objects.create(**group_data)
            found_pet.group = group

        traits = serializer.validated_data.pop("traits", None)
        if traits:
            trait_obj = []
            for trait_data in traits:
                try:
                    trait = Trait.objects.get(name__iexact=trait_data["name"])
                except Trait.DoesNotExist:
                    trait = Trait.objects.create(**trait_data)
                trait_obj.append(trait)
            found_pet.traits.set(trait_obj)

        for (
            key,
            value,
        ) in serializer.validated_data.items():
            setattr(found_pet, key, value)
        found_pet.save()

        serializer = PetSerializer(found_pet)
        return Response(serializer.data)
