from starlette.responses import JSONResponse


class MessageOk:
    @classmethod
    def excluir_refin(cls):
        return JSONResponse(status_code=201, content={
            "competenciaInicioDesconto": 202102,
            "listaContratosReativados": [
                {
                    "numeroContrato": "C_8011069347_1061"
                },
                {
                    "numeroContrato": "C_8011069347_1062"
                }
            ],
            "mensagem": "Inclusão efetuada com sucesso",
            "numeroContrato": "C_8011069347_1064",
            "codigoSucesso": "BD",
            "hashOperacao": 735645})
