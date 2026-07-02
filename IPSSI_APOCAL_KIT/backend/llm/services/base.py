"""Interface abstraite pour un client LLM générateur de quiz."""

from abc import ABC, abstractmethod


class LLMClient(ABC):
    """Interface commune à Ollama / Mock / autres backends futurs.

    Le contrat : `generate_quiz` reçoit un texte source et renvoie une liste
    de 10 dicts (prompt, options[4], correct_index) — structure validée par
    le générateur en amont du save en DB.
    """

    @abstractmethod
    def generate_quiz(self, source_text: str, title: str) -> list[dict]:
        """Renvoie 10 questions QCM générées à partir du texte source.

        Raises:
            LLMError: si le LLM est indisponible, lent, ou renvoie une
                      structure invalide qui ne peut être réparée.
        """
        raise NotImplementedError


class LLMError(Exception):
    """Erreur générique côté LLM (indisponibilité, parsing, validation)."""


class QuizValidationError(LLMError):
    """Sortie LLM structurellement/contenu invalide (échec de la validation J3).

    Sous-classe de LLMError : tout code qui n'attrape que `LLMError` continue de
    fonctionner. On la DISTINGUE pour la couche 4 (re-prompt) : on RÉ-ESSAIE sur
    une erreur de validation (le modèle peut mieux faire au 2ᵉ essai), mais PAS
    sur une erreur de transport (LLM injoignable → retenter est inutile).
    """
