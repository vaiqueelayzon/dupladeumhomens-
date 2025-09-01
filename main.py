from fastapi import FastAPI

app = FastAPI(title='Livro de receitas do layzon')




receitas = [
    {
        'nome': 'brownie',
        'ingredientes': ['3 Ovos', '6 colheres de açúcar', '200g de chocolate', '100g de manteiga'],
        'utensílios': ['tijela', 'forma', 'colher'],
        'modo de preparo': 'Misture tudo, despeje na forma e asse por 30 minutos.',
    },
    {
        'nome': 'torta',
        'ingredientes': ['3 Ovos', '6 colheres de açúcar', '1 xícara de farinha', '1/2 xícara de leite'],
        'utensílios': ['tijela', 'forma', 'batedeira'],
        'modo de preparo': 'Bata os ingredientes, leve ao forno até dourar.',
    },
    {
        'nome': 'bolo de cenoura',
        'ingredientes': ['3 cenouras médias', '4 ovos', '1 xícara de óleo', '2 xícaras de açúcar', '2 xícaras de farinha'],
        'utensílios': ['liquidificador', 'forma', 'peneira'],
        'modo de preparo': 'Bata os líquidos, misture com os secos e asse por 40 minutos.',
    },
    {
        'nome': 'panqueca',
        'ingredientes': ['2 ovos', '1 xícara de leite', '1 xícara de farinha', '1 pitada de sal'],
        'utensílios': ['frigideira', 'concha', 'tigela'],
        'modo de preparo': 'Misture tudo e frite porções pequenas na frigideira.',
    },
    {
        'nome': 'pudim',
        'ingredientes': ['1 lata de leite condensado', '2 latas de leite', '3 ovos'],
        'utensílios': ['liquidificador', 'forma de pudim', 'panela para banho-maria'],
        'modo de preparo': 'Bata tudo no liquidificador, despeje na forma e asse em banho-maria por 1 hora.',
    },
    {
        'nome': 'cookies',
        'ingredientes': ['2 xícaras de farinha', '1 xícara de açúcar', '1 ovo', '100g de manteiga', 'gotas de chocolate'],
        'utensílios': ['tigela', 'forma', 'colher'],
        'modo de preparo': 'Misture os ingredientes, molde os cookies e asse por 15 minutos.',
    },
]

@app.get("/receitas")
def listar_receitas():
    return receitas

@app.get("/receitas/(nome)")
def buscar_receitas (nome: str):
    for receitas in receitas:
        if receitas['nome'].lower() == nome.lower():
            return receitas
        return {"erro": "Receitas nao encontrada"}