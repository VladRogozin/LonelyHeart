from django.contrib import admin, messages
from .models import Cat, Blog, Cards, OurNumbers, CustomersForm


class CatAdmin(admin.ModelAdmin):



    def save_model(self, request, obj, form, change):
        # Отправляем предупреждение перед сохранением
        messages.warning(request, 'Нагадую що бажано зберігати зображення котів 16:9 ! (це можна відформатувати в телефоні у будь-якому редакторі) Такі зображення будуть виглядати набагато краще на самий сторінці.')
        # Вызываем оригинальный метод save_model для сохранения модели
        super().save_model(request, obj, form, change)


class CustomersFormAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['phone_number'].label = "Номер телефона"
        form.base_fields['name'].label = "Як до вас можна звертатись?"
        form.base_fields['social_media_account'].label = "Якою соц.мережею ви користуєтесь"
        form.base_fields['address'].label = "Ваше місце проживання (назва населеного пункту та область)"
        form.base_fields['housing_type'].label = "Ви живете в"
        form.base_fields['living_arrangement'].label = "Ви шукаєте тваринку для проживання в:"
        form.base_fields['rental_status'].label = "Чи ви є власником житла в якому мешкаєте?"
        form.base_fields['desired_pet_age'].label = "Який вік тваринки ви розглядаєте"
        form.base_fields['pet_care_experience'].label = "Чи маєте досвід в утриманні тваринки?"
        form.base_fields['previous_pet_experience'].label = "Якою тваринкою ви опікувались раніше ?"
        form.base_fields['your_experienc_keeping_animals'].label = "Розкажіть про ваш досвід в утриманні тваринок. Як утримувались котики. "
        form.base_fields['how_old_was_your_last_pet'].label = "В якому віці була ваша остання тваринка?"
        form.base_fields['current_pets'].label = "Чи  проживають зараз з вами інші тварини? Вкажіть вид, вік, стать, стерилізована чи ні, породу (якщо є)."
        form.base_fields['feeding_knowledge'].label = "Що ви знаєте про гoдування тварини?"
        form.base_fields['neutering_spaying_attitude'].label = "Ваше ставлення до кастрації\стерилізації?"
        form.base_fields['vaccination_attitude'].label = "Яке ваше ставлення до щеплення та які  проводили щеплення своєї попередньої тваринки?"
        form.base_fields['outdoor_cat_attitude'].label = "Як ви ставитесь до того, щоб котик гуляв на подвір'ї  будинку?"
        form.base_fields['rules_for_keeping_dog_cat'].label = "Що ви знаєте про правила утримання собаки/котика? Дайте розгорнуту відповідь."
        form.base_fields['dog_house_knowledge'].label = "Де має проживати собака в приватному будинку?"
        form.base_fields['decide_to_adopta_cat_dog'].label = "Чому ви вирішили взяти саме Котика\Песика?  Які задачі\функції має виконувати собака\котик?  "
        form.base_fields['dog_training_goals'].label = "Що має знати\вміти  собака\киця на момент адопції?"
        form.base_fields['daily_time_commitment'].label = "Як багато часу в день ви можете приділити тваринці?"
        form.base_fields['emergency_contact'].label = "Чи маєте довірену особу, яка зможе піклуватись про тваринку на час вашої відсутності?"
        form.base_fields['animal_with_health_roblems'].label = "Чи готові ви взяти тваринку з проблемами по здоров'ю?"
        form.base_fields['ready_for_additional_expenses'].label = "Чи готові ви  до додаткових витрат, якщо тваринка захворіє?"
        form.base_fields['animal_problematic_personality'].label = "Чи готові ви до тваринки з проблемним характером  або проблемною поведінкою?"
        form.base_fields['consultations_behavioral_specialists'].label = "Чи готові ви до додаткових витрат на консультації спеціалістів з коррекції поведінки..."
        form.base_fields['animal_may_scratch_bite_whine'].label = "Чи готові до того, що тваринка до певного віку і певний період часу, може дряпатись, кусатись, скавчати\мявчати чи бігати по ночах?"
        form.base_fields['children_in_home'].label = "Чи є у вашій в родині є діти, вкажіть їх вік."
        form.base_fields['children_lived_animals'].label = "Чи жили ваші діти з тваринами раніше? Якщо так, то з якими тваринами та як довго? Дайте розгорнену відповідь. "
        form.base_fields['everyone_ready_for'].label = "Чи всі готові до нового члена родини??"
        form.base_fields['home_floor'].label = "На якому поверсі ви проживаєте? Як захищені вікна від випадіння кота? (якщо обираєте собаку ставте прочерк)"
        form.base_fields['Im_ready_for_puddles_and_piles_at_home'].label = "Чи згодні ви з висловом: Я готовий до луж та купок вдома"
        form.base_fields['prepared_fact_animal_can_spoil_your_roperty'].label = "Чи готові до того, що тваринка може зіпсувати ваше майно та цінні речі?"
        form.base_fields['how_do_you_see_your_animal'].label = "Якою ви бачите свою тваринку?"
        form.base_fields['travel_plans'].label = "Якщо доведеться транспортувати тваринку, як плануєте це робити?"
        form.base_fields['how_do_you_give_up_an_animal'].label = "Що може змусити вас відмовитись від спільного проживання з тваринкою ( в його утриманні)"
        form.base_fields['ready_to_provide_photo_video_of_apartment'].label = "Якщо ви обрали песика** Чи готові ви надати фото\відео  помешкання або теріторії і вол'єру, щоб ми могли перевірити умови  для майбутнього проживання тварини?"
        form.base_fields['signing_an_official_contract_passport'].label = "Всі наші тваринки віддаються після підписання офіційного договору з занесенням в нього паспортних  даних"
        form.base_fields['photo_video_reports_of_your_pet'].label = "Чи готові ви підтримувати зв'язок з нами і  радувати нас фото/відео звітами вашого улюбленця?"
        form.base_fields['how_did_you_find_out_about_our_shelter'].label = "Звідки ви дізналися  про наш притулок ?"
        form.base_fields['application_approved'].label = "Я даю згоду на обробку, зберігання та використання, згідно Закону України «Про захист персональних даних», своїх персональних даних, вказаних у цій Анкеті."




        return form



admin.site.register(OurNumbers, CatAdmin)
admin.site.register(CustomersForm, CustomersFormAdmin)
admin.site.register(Cards, CatAdmin)
admin.site.register(Cat, CatAdmin)
admin.site.register(Blog, CatAdmin)
