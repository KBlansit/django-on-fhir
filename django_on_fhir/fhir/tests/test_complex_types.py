from django.test import TestCase

# complex_types
from fhir.models.complex_types.address import Address, AddressFhirString
from fhir.models.complex_types.annotation import Annotation
from fhir.models.complex_types.attachment import Attachment
from fhir.models.complex_types.codeable_concept import CodeableConcept, CodeableConceptCoding
from fhir.models.complex_types.coding import Coding
from fhir.models.complex_types.contact_point import ContactPoint
from fhir.models.complex_types.human_name import HumanName, HumanNameFamily, HumanNameGiven\
    , HumanNameSuffix
from fhir.models.complex_types.identifier import Identifier
from fhir.models.complex_types.period import Period
from fhir.models.complex_types.quantity import Quantity
from fhir.models.complex_types.range import Range
from fhir.models.complex_types.ratio import Ratio
from fhir.models.complex_types.sampled_data import SampledData
from fhir.models.complex_types.signature import Signature
from fhir.models.complex_types.simple_quantity import SimpleQuantity
from fhir.models.complex_types.timing import Timing, RepeatTiming

class AddressTestCase(TestCase):
    def setUp(self):
        self.test_address = Address()
        self.test_address.save()

    def test_can_add_multiple_address_lines(self):

        test_lst = [
            "White House",
            "Oval Office",
            "1600 Pennsylvania Ave NW",
            "District of Columbia",
            "20500",
        ]

        # make list of AddressFhirString objects
        obj_lst = [AddressFhirString(string=x) for x in test_lst]
        [x.save() for x in obj_lst]
        [x.address.add(self.test_address) for x in obj_lst]

        for x in Address.objects.get(pk=1).addressfhirstring_set.all():
            self.assertIn(str(x.string), test_lst)

class AnnotationTestCase(TestCase):
    pass

class AttachmentTestCase(TestCase):
    pass

class CodeableConceptTestCase(TestCase):
    pass

class CodingTestCase(TestCase):
    pass

class ContactPointTestCase(TestCase):
    pass

class HumanNameTestCase(TestCase):
    pass

class IdentifierTestCase(TestCase):
    pass

class PeriodTestCase(TestCase):
    pass

class QuantityTestCase(TestCase):
    pass

class RangeTestCase(TestCase):
    pass

class RatioTestCase(TestCase):
    pass

class SampledDataTestCase(TestCase):
    pass

class SignatureTestCase(TestCase):
    pass

class SimpleQuantityTestCase(TestCase):
    pass

class TimingTestCase(TestCase):
    pass
