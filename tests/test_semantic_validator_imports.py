def test_semantic_validator_imports_without_ast_documentnode():
    from vsa.semantic_validator import SemanticValidator

    assert SemanticValidator is not None
