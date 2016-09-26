rom django.test import TestCase

class AddressTestCase(TestCase):
    from fhir.models.complex_types.address import Address

class AnnotationTestCase(TestCase):
    from fhir.models.complex_types.annotation import Annotation

class AttachmentTestCase(TestCase):
    from fhir.models.complex_types.attachment import Attachment

class CodeableConceptTestCase(TestCase):
    from fhir.models.complex_types.codeable_concept import CodeableConcept

class CodingTestCase(TestCase):
    from fhir.models.complex_types.coding import Coding

class HumanNameTestCase(TestCase):
    from fhir.models.complex_types.human_name import HumanName

class IdentifierTestCase(TestCase):
    from fhir.models.complex_types.identifier import Identifier

class PeriodTestCase(TestCase):
    from fhir.models.complex_types.period import Period

class QuantityTestCase(TestCase):
    from fhir.models.complex_types.quantity import Quantity

class RangeTestCase(TestCase):
    from fhir.models.complex_types.range import Range

class RatioTestCase(TestCase):
    from fhir.models.complex_types.ratio import Ratio

class SampledDataTestCase(TestCase):
    from fhir.models.complex_types.sampled_data import SampledData

class SignatureTestCase(TestCase):
    from fhir.models.complex_types.signature import Signature

class SimpleQuantityTestCase(TestCase):
    from fhir.models.complex_types.simple_quantity import SimpleQuantity

class TimingTestCase(TestCase):
    from fhir.models.complex_types.timing import Timing
