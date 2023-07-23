from django.db import models


from django.db import models

class Cat(models.Model):
    PET_CHOICES = [
        ('Cat', 'Cat'),
        ('Dog', 'Dog'),
        ('Yoang Cat', 'Yoang Cat'),
        ('Kitten', 'Kitten'),
    ]

    what_kind_of_pet = models.CharField(max_length=100, choices=PET_CHOICES, default='Cat')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, default='men')
    sick = models.CharField(max_length=100, default=' ')
    character = models.CharField(max_length=100, default='не визначено')
    friendliness = models.CharField(max_length=100, default='не визначено')
    features = models.TextField()
    tactility = models.CharField(max_length=100, default='не визначено')
    color = models.CharField(max_length=50)
    sterilization = models.CharField(max_length=50, default='Не стерилізовані')
    vaccination = models.CharField(max_length=50, default='Не вакциновані')
    peculiarity = models.CharField(max_length=100, default='не визначено')

    photo_1 = models.ImageField(upload_to='cat_photos/', default='')
    photo_2 = models.ImageField(upload_to='cat_photos/', default='')
    photo_3 = models.ImageField(upload_to='cat_photos/', default='')

    video_link = models.URLField(max_length=200, default='')

    class Meta:
        app_label = 'cat'

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField()
    photo = models.ImageField(upload_to='blog_photos/')

    def __str__(self):
        return self.title


class Cards(models.Model):
    name_on_card = models.CharField(max_length=50, default=' ')
    name_bank_card = models.CharField(max_length=50, default=' ')
    privar_one = models.CharField(max_length=20)


class OurNumbers(models.Model):
    cats = models.IntegerField()
    dogs = models.IntegerField()
    food = models.IntegerField()
    debt = models.IntegerField(default=0)


class CustomersForm(models.Model):
    name = models.CharField(max_length=500, default=' ')
    phone_number = models.CharField(max_length=10, default=' ')
    social_media_account = models.CharField(max_length=500, default=' ')
    address = models.CharField(max_length=500, default=' ')
    housing_type = models.CharField(max_length=500, default=' ')
    living_arrangement = models.CharField(max_length=500, default=' ')
    rental_status = models.CharField(max_length=500, default=' ')
    desired_pet_age = models.CharField(max_length=500, default=' ')
    pet_care_experience = models.CharField(max_length=500, default=' ')
    previous_pet_experience = models.CharField(max_length=500, default=' ')
    your_experienc_keeping_animals = models.CharField(max_length=500, default=' ')
    how_old_was_your_last_pet = models.CharField(max_length=500, default=' ')
    current_pets = models.CharField(max_length=500, default=' ')
    feeding_knowledge = models.CharField(max_length=500, default=' ')
    neutering_spaying_attitude = models.CharField(max_length=500, default=' ')
    vaccination_attitude = models.CharField(max_length=500, default=' ')
    outdoor_cat_attitude = models.CharField(max_length=500, default=' ')
    rules_for_keeping_dog_cat = models.CharField(max_length=500, default=' ')
    dog_house_knowledge = models.CharField(max_length=500, default=' ')
    decide_to_adopta_cat_dog = models.CharField(max_length=500, default=' ')
    dog_training_goals = models.CharField(max_length=500, default=' ')
    daily_time_commitment = models.CharField(max_length=500, default=' ')

    emergency_contact = models.CharField(max_length=500, default=' ')
    animal_with_health_roblems = models.CharField(max_length=500, default=' ')
    ready_for_additional_expenses = models.CharField(max_length=500, default=' ')
    animal_problematic_personality = models.CharField(max_length=500, default=' ')
    consultations_behavioral_specialists = models.CharField(max_length=500, default=' ')
    animal_may_scratch_bite_whine = models.CharField(max_length=500, default=' ')
    children_in_home = models.CharField(max_length=500, default=' ')
    children_lived_animals = models.CharField(max_length=500, default=' ')
    everyone_ready_for = models.CharField(max_length=500, default=' ')
    home_floor = models.CharField(max_length=500, default=' ')
    Im_ready_for_puddles_and_piles_at_home = models.CharField(max_length=500, default=' ')
    prepared_fact_animal_can_spoil_your_roperty = models.CharField(max_length=500, default=' ')
    how_do_you_see_your_animal = models.CharField(max_length=500, default=' ')
    travel_plans = models.CharField(max_length=500, default=' ')
    how_do_you_give_up_an_animal = models.CharField(max_length=500, default=' ')
    ready_to_provide_photo_video_of_apartment = models.CharField(max_length=500, default=' ')
    signing_an_official_contract_passport = models.CharField(max_length=500, default=' ')
    photo_video_reports_of_your_pet = models.CharField(max_length=500, default=' ')
    how_did_you_find_out_about_our_shelter = models.CharField(max_length=500, default=' ')
    application_approved = models.CharField(max_length=100, default=' ')

