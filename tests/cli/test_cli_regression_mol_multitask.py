"""This tests the CLI functionality of training and predicting a regression model on a single molecule.
"""

import pytest

from chemprop2.cli.main import main

pytestmark = pytest.mark.CLI


@pytest.fixture
def data_path(data_dir):
    return str(data_dir / "regression" / "mol_multitask.csv")


@pytest.fixture
def model_path(data_dir):
    return str(data_dir / "example_model_v2_regression_mol_multitask.pt")


def test_train_quick(monkeypatch, data_path):
    args = [
        "chemprop2",
        "train",
        "-i",
        data_path,
        "--epochs",
        "3",
        "--num-workers",
        "0",
        "--show-individual-scores",
    ]

    with monkeypatch.context() as m:
        m.setattr("sys.argv", args)
        main()


def test_predict_quick(monkeypatch, data_path, model_path):
    args = ["chemprop2", "predict", "-i", data_path, "--model-path", model_path]

    with monkeypatch.context() as m:
        m.setattr("sys.argv", args)
        main()

    args = ["chemprop2", "predict", "-i", data_path, "--model-path", model_path]

    with monkeypatch.context() as m:
        m.setattr("sys.argv", args)
        main()


@pytest.mark.parametrize("ffn_block_index", ["0", "1"])
def test_fingerprint_quick(monkeypatch, data_path, model_path, ffn_block_index):
    args = [
        "chemprop2",
        "fingerprint",
        "-i",
        data_path,
        "--model-path",
        model_path,
        "--ffn-block-index",
        ffn_block_index,
    ]

    with monkeypatch.context() as m:
        m.setattr("sys.argv", args)
        main()
