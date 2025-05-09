from dataclasses import dataclass, field

from rdkit.Chem.rdchem import Atom, Bond

from chemprop2.featurizers.atom import MultiHotAtomFeaturizer
from chemprop2.featurizers.base import VectorFeaturizer
from chemprop2.featurizers.bond import MultiHotBondFeaturizer


@dataclass
class _MolGraphFeaturizerMixin:
    atom_featurizer: VectorFeaturizer[Atom] = field(default_factory=MultiHotAtomFeaturizer.v2)
    bond_featurizer: VectorFeaturizer[Bond] = field(default_factory=MultiHotBondFeaturizer)

    def __post_init__(self):
        self.atom_fdim = len(self.atom_featurizer)
        self.bond_fdim = len(self.bond_featurizer)

    @property
    def shape(self) -> tuple[int, int]:
        """the feature dimension of the atoms and bonds, respectively, of `MolGraph`s generated by
        this featurizer"""
        return self.atom_fdim, self.bond_fdim
