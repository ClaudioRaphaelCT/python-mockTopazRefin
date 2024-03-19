from modules.excluir_refin.messages.messages_ok import MessageOk
from modules.excluir_refin.messages.messages_error import MessageError
from modules.excluir_refin.Model.Refin_body import NumeroBeneficio


class Refin:
    @classmethod
    def get(cls, numeroBeneficio: NumeroBeneficio = None):
        if numeroBeneficio is None or numeroBeneficio.numeroBeneficio is None:
            return MessageError.empty()
        if numeroBeneficio.numeroBeneficio == 34184742510:
            return MessageError.access()
        return MessageOk.excluir_refin()
