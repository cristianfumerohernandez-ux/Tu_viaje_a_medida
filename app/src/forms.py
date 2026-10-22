from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, BooleanField
from wtforms.validators import Optional, NumberRange

ENVIRONMENTS = [
    ("", "Cualquiera"),
    ("playa", "Playa"),
    ("montaña", "Montaña"),
    ("ciudad", "Ciudad"),
]

ACCOMMODATION_TYPES = [
    ("", "Cualquiera"),
    ("hotel", "Hotel"),
    ("hostal", "Hostal"),
    ("cabaña", "Cabaña"),
    ("apartamento", "Apartamento"),
]


class BaseSearchForm(FlaskForm):
    class Meta:
        csrf = False  # formulario de solo consulta: no necesita CSRF


class DestinationSearchForm(BaseSearchForm):
    environment = SelectField("Entorno", choices=ENVIRONMENTS,
                              validators=[Optional()])
    no_visa = BooleanField("Solo destinos sin visado previo")


class AccommodationSearchForm(BaseSearchForm):
    type = SelectField("Tipo de alojamiento", choices=ACCOMMODATION_TYPES,
                       validators=[Optional()])
    max_price = IntegerField(
        "Máximo por noche (€)",
        validators=[Optional(),
                    NumberRange(min=0, max=10000,
                                message="El precio debe estar entre 0 y 10000 €.")],
    )
    breakfast = BooleanField("Desayuno incluido")
    pets = BooleanField("Admite mascotas")


class TailoredTripForm(BaseSearchForm):
    environment = SelectField("Entorno", choices=ENVIRONMENTS,
                              validators=[Optional()])
    no_visa = BooleanField("Solo destinos sin visado previo")
    type = SelectField("Tipo de alojamiento", choices=ACCOMMODATION_TYPES,
                       validators=[Optional()])
    max_price = IntegerField(
        "Máximo por noche (€)",
        validators=[Optional(),
                    NumberRange(min=0, max=10000,
                                message="El precio debe estar entre 0 y 10000 €.")],
    )
    breakfast = BooleanField("Desayuno incluido")


def get_search_form(mode):
    return {
        "destinos": DestinationSearchForm,
        "alojamientos": AccommodationSearchForm,
        "medida": TailoredTripForm,
    }[mode]