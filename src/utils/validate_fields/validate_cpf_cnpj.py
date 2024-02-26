from validate_docbr import CNPJ, CPF


def validate_cpf_cnpj(value, doc_type):
    if doc_type == 'cpf':
        cpf = CPF()
        return cpf.validate(value)
    elif doc_type == 'cnpj':
        cnpj = CNPJ()
        return cnpj.validate(value)
    else:
        return False