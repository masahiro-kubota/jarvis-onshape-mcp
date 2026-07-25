from __future__ import annotations

from onshape_mcp.api.sketch_inspect import inspect_sketch


def test_inspect_sketch_labels_entity_coordinates_as_definition_seed():
    features_doc = {
        "features": [
            {
                "btType": "BTMSketch-151",
                "featureId": "sketch-1",
                "name": "profile",
                "parameters": [],
                "entities": [],
                "constraints": [],
            }
        ],
        "featureStates": {
            "sketch-1": {"featureStatus": "OK"},
        },
    }

    result = inspect_sketch(features_doc, sketch_feature_id="sketch-1")

    assert result["entity_geometry_basis"] == "definition_seed"
    assert "pre-solve seed values" in result["entity_geometry_note"]
    assert "not solver-resolved" in result["text"]
