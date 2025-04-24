"""Global configuration variables for chemprop2"""

from chemprop2.featurizers.molgraph.molecule import SimpleMoleculeMolGraphFeaturizer

DEFAULT_ATOM_FDIM, DEFAULT_BOND_FDIM = SimpleMoleculeMolGraphFeaturizer().shape
DEFAULT_HIDDEN_DIM = 300
