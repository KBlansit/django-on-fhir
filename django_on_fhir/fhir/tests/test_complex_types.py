from django.test import TestCase

# complex_types
from complex_types.address import Address, AddressFhirString
from complex_types.annotation import Annotation
from complex_types.attachment import Attachment
from complex_types.codeable_concept import CodeableConcept, CodeableConceptCoding
from complex_types.coding import Coding
from complex_types.contact_point import ContactPoint
from complex_types.human_name import HumanName, HumanNameFamily, HumanNameGiven\
    , HumanNameSuffix
from complex_types.identifier import Identifier
from complex_types.period import Period
from complex_types.quantity import Quantity
from complex_types.range import Range
from complex_types.ratio import Ratio
from complex_types.sampled_data import SampledData
from complex_types.signature import Signature
from complex_types.simple_quantity import SimpleQuantity
from complex_types.timing import Timing, RepeatTiming

class AddressTestCase(TestCase):
    def setUp(self):
        Address.objects.create()

    def test_can_add_multiple_address_lines(self):
        
    def test_use_choices(self):

    def test_type_choices(self):

class AnnotationTestCase(TestCase):

class AttachmentTestCase(TestCase):

class CodeableConceptTestCase(TestCase):

class CodingTestCase(TestCase):

class ContactPointTestCase(TestCase):

class HumanNameTestCase(TestCase):

class IdentifierTestCase(TestCase):

class PeriodTestCase(TestCase):

class QuantityTestCase(TestCase):

class RangeTestCase(TestCase):

class RatioTestCase(TestCase):

class SampledDataTestCase(TestCase):

class SignatureTestCase(TestCase):

class SimpleQuantityTestCase(TestCase):

class TimingTestCase(TestCase):
