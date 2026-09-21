import pytest
from pydantic import ValidationError

from src.models.domain.document import Document


def make_doc(**overrides):
    data = {
        "doc_id": "abc",
        "text": "hello",
        "source_path": "datasets/ZX Bank/md/a.md",
        "file_format": "md",
        "enterprise": "ZX Bank",
        "title": "A",
    }
    data.update(overrides)
    return Document(**data)


def test_make_id_is_stable():
    a = Document.make_id("ZX Bank", "a/b.md")
    b = Document.make_id("ZX Bank", "a/b.md")
    assert a == b
    assert len(a) == 16


def test_make_id_differs_for_different_paths():
    a = Document.make_id("ZX Bank", "a/b.md")
    c = Document.make_id("ZX Bank", "a/c.md")
    assert a != c


def test_make_id_differs_for_different_enterprises():
    a = Document.make_id("ZX Bank", "a/b.md")
    b = Document.make_id("CloudWay-24", "a/b.md")
    assert a != b


def test_empty_text_is_rejected():
    with pytest.raises(ValidationError):
        make_doc(text="")


def test_missing_required_field_is_rejected():
    with pytest.raises(ValidationError):
        Document(text="hi")


def test_document_is_immutable():
    doc = make_doc()
    with pytest.raises(ValidationError):
        doc.text = "changed"


def test_metadata_defaults_to_separate_empty_dicts():
    a = make_doc()
    b = make_doc()
    assert a.metadata == {}
    assert a.metadata is not b.metadata
