import random

banco_de_questoes = [
    {
        "matéria": "Matemática",
        "pergunta": "Qual o valor de x na equação 3x - 9 = 0?",
        "opcao": ["A) x = 1", "B) x = 3", "C) x = 9", "D) x = 0"],
        "correta": "B"
        },
    {
        "matéria": "Matemática",
        "pergunta": "Qual desses é um número ímpar?",
        "opcao": ["A) 2", "B) 17388", "C) 3", "D) 10"],
        "correta": "C"
        },
    {
        "matéria": "Matemática",
        "pergunta": "Uma função é dada por f(x) = 2x + 1. Calcule f se x fosse 3",
        "opcao": ["A) 7", "B) 6", "C) 5", "D) 8"],
        "correta": "A"
        },
    {
        "matéria": "Matemática",
        "pergunta": "A raiz quadrada de 144 é:",
        "opcao": ["A) 11", "B) 10", "C)13", "D)12"],
        "correta": "D"
        },
    {
        "matéria": "Matemática",
        "pergunta": "3² + 4² é igual a:",
        "opcao": ["A)25", "B)15", "C)11", "D)5"],
        "correta": "A"
        },
    {
        "matéria": "Matemática",
        "pergunta": "Se x=2, então 3x² é igual a:",
        "opcao": ["A)8", "B)6", "C)12", "D)10"],
        "correta": "C"
        },
    {
        "matéria": "Matemática",
        "pergunta": "25% de 80 é:",
        "opcao": ["A)20", "B)15", "C)21", "D)37"],
        "correta": "A"
        },
    {
        "matéria": "Matemática",
        "pergunta": "Um ângulo reto mede:",
        "opcao": ["A)60°", "B)360°", "C)180°", "D)90°"],
        "correta": "D"
        },
    {
        "matéria": "Matemática",
        "pergunta": "Resolva 5x = 20",
        "opcao": ["A)3", "B)4", "C)10", "D)20"],
        "correta": "B"
        },
    {
        "matéria": "Matemática",
        "pergunta": "A média de 6,8 e 10 é:",
        "opcao": ["A)7", "B)10", "C)8", "D)67"],
        "correta": "C"
        },
    {
        "matéria": "História",
        "pergunta": "A independência do Brasil ocorreu no contexto:",
        "opcao": ["A) da Revolução Industrial", "B) das Revoluções Liberais", "C) do Feudalismo", "D) da Guerra Fria"],
        "correta": "B"
        },
    {
        "matéria": "História",
        "pergunta": "A Lei Áurea foi assinada:",
        "opcao": ["A) por Dom Pedro I", "B) por Stalin", "C) por Getúlio Vargas", "D) pela Princesa Isabel"],
        "correta": "D"
        },
    {
        "matéria": "História",
        "pergunta": "O iluminismo defendia:",
        "opcao": ["A) a razão e a ciência", "B) poder absoluto ao rei", "C) o feudalismo", "D) a escravidão"],
        "correta": "A"
        },
    {
        "matéria": "História",
        "pergunta": "A Revolução Francesa tinha como lema:",
        "opcao": ["A) Ordem e Progresso", "B) Fé e poder", "C) Liberdade, Igualdade e Fraternidade", "D) Liberdade e Igualdade para as Mulheres"],
        "correta": "C"
        },
    {
        "matéria": "História",
        "pergunta": "O período colonial brasileiro foi marcado por:",
        "opcao": ["A)i ndustrialização", "B) democracia", "C) agricultura e exportação", "D) Celulares e televisões"],
        "correta": "C"
        },
    {
        "matéria": "História",
        "pergunta": "A República Velha foi dominada por:",
        "opcao": ["A) elite agrárias", "B) comerciantes", "C) militares", "D) aldeões"],
        "correta": "A"
        },
    {
        "matéria": "História",
        "pergunta": "Uma das causas da Primeira Guerra Mundial foi:",
        "opcao": ["A)tecnologia", "B)disputas imperialistas", "C)clima", "D)religião"],
        "correta": "B"
        },
    {
        "matéria": "História",
        "pergunta": "Getúlio Vargas governou:",
        "opcao": ["A)como um rei", "B)como um militar", "C)apenas no exterior", "D)em regimes autoritários e democráticos"],
        "correta": "D"
        },
    {
        "matéria": "História",
        "pergunta": "A Guerra Fria foi marcada por:",
        "opcao": ["A)guerra indireta", "B)colonização", "C)paz total", "D)disputa ideológica"],
        "correta": "D"
        },
    {
        "matéria": "História",
        "pergunta": "A urbanização no Brasil aumentou principalmente:",
        "opcao": ["A)no século XXI", "B)no século XIX", "C)no século XX", "D)na Idade Média"],
        "correta": "C"
        },
    {
        "matéria": "Ciências",
        "pergunta": "A fotossíntese transforma:",
        "opcao": ["A)energia química em luz", "B)luz em energia química", "C)calor em luz", "D)água em fogo"],
        "correta": "B"
        },
    {
        "matéria": "Ciências",
        "pergunta": "O sistema nersovo é responsável por:",
        "opcao": ["A)digestão", "B)coordenação do corpo", "C)respiração", "D)circulação"],
        "correta": "B"
        },
    {
        "matéria": "Ciências",
        "pergunta": "A ebulição da água ocorre a:",
        "opcao": ["A)0°", "B)180°", "C)200°", "D)100°"],
        "correta": "D"
        },
    {
        "matéria": "Ciências",
        "pergunta": "A célula é:",
        "opcao": ["A)unidade de vida", "B)sistema", "C)pele", "D)tecido"],
        "correta": "A"
        },
    {
        "matéria": "Ciências",
        "pergunta": "O coração bombeia:",
        "opcao": ["A)ar", "B)células", "C)sangue", "D)ossos"],
        "correta": "C"
        },
    {
        "matéria": "Ciências",
        "pergunta": "A força da gravidade:",
        "opcao": ["A)destrói universos", "B)atrai objetos", "C)repele objetos", "D)não atua em nada"],
        "correta": "B"
        },
    {
        "matéria": "Ciências",
        "pergunta": "A energia elétrica pode ser transformada em:",
        "opcao": ["A)luz", "B)calor", "C)movimento", "D)todas as anteriores"],
        "correta": "D"
        },
    {
        "matéria": "Ciências",
        "pergunta": "O pulmão realiza:",
        "opcao": ["A)digestão", "B)circulação", "C)respiração", "D)excreção"],
        "correta": "C"
        },
    {
        "matéria": "Ciências",
        "pergunta": "O planeta mais próximo do Sol é:",
        "opcao": ["A)Terra", "B)Marte", "C)Mercúrio", "D)Vênus"],
        "correta": "C"
        },
    {
        "matéria": "Ciências",
        "pergunta": "A Água no estado sólido é:",
        "opcao": ["A)vapor", "B)líquido", "C)gás", "D)gelo"],
        "correta": "D"
        },
    {
        "matéria": "Geografia",
        "pergunta": "A globalização está ligada a:",
        "opcao": ["A)isolamento", "B)integração mundial", "C)terceira guerra mundial", "D)divisão multinacional"],
        "correta": "B"
        },
    {
        "matéria": "Geografia",
        "pergunta": "O clima equatorial é:",
        "opcao": ["A)quente e úmido", "B)frio e pluvioso", "C)calor moderado e frio intenso", "D)calor intenso e frio moderado"],
        "correta": "A"
        },
    {
        "matéria": "Geografia",
        "pergunta": "A industrialização causa:",
        "opcao": ["A)diminuição urbana", "B)aumento urbano", "C)menos empregos", "D)mais empregos"],
        "correta": "B"
        },
    {
        "matéria": "Geografia",
        "pergunta": "A população urbana vive:",
        "opcao": ["A)no campo", "B)na floresta", "C)nas cidades", "D)no deserto"],
        "correta": "C"
        },
    {
        "matéria": "Geografia",
        "pergunta": "O MercoSul é:",
        "opcao": ["A)um país", "B)um continente", "C)um bloco econômico", "D)um dos maiores oceanos"],
        "correta": "C"
        },
    {
        "matéria": "Geografia",
        "pergunta": "A Latitude mede:",
        "opcao": ["A)a distância do meridiano", "B)a distância do Equador", "C)a altitude", "D)o relevo"],
        "correta": "B"
        },
    {
        "matéria": "Geografia",
        "pergunta": "O desmatamento causa:",
        "opcao": ["A)aumento de florestas", "B)perda de biodiversidade", "C)mais chuvas", "D)menos impactos aos animais"],
        "correta": "B"
        },
    {
        "matéria": "Geografia",
        "pergunta": "O relevo montanhoso possui:",
        "opcao": ["A)oceanos enormes", "B)áreas planas", "C)grandes elevações", "D)desertos, como o Saara"],
        "correta": "C"
        },
    {
        "matéria": "Geografia",
        "pergunta": "O Brasil é considerado:",
        "opcao": ["A)um país desenvolvido", "B)um país subdesenvolvido", "C)um país emergente", "D)um país localizado nos Estados Unidos"],
        "correta": "C"
        },
    {
        "matéria": "Geografia",
        "pergunta": "A urbanização desordenada pode causar:",
        "opcao": ["A)grande organização", "B)equilíbrio político", "C)poluição", "D)nada"],
        "correta": "C"
        },
    {
        "matéria": "Português",
        "pergunta": "Leia 'Apesar da chuva, ele foi ao treino.', a conjução 'apesar de' indica:",
        "opcao": ["A)causa", "B)finalidade", "C)consequência", "D)oposição"],
        "correta": "D"
        },
    {
        "matéria": "Português",
        "pergunta": "Na frase 'Fazem dois anos que estudo aqui', o verbo está",
        "opcao": ["A)No subjuntivo", "B)No futuro", "C)Incorreta, pois deveria ser Faz", "D)No presente"],
        "correta": "C"
        },
    {
        "matéria": "Português",
        "pergunta": "Qual das frases a seguir possui uma linguagem conotativa?",
        "opcao": ["A)O Sol nasceu as 6h", "B)Ele é uma fera jogando futebol", "C)Comprei um caderno", "D)A Água está gelada"],
        "correta": "B"
        },
    {
        "matéria": "Português",
        "pergunta": "Na frase 'Se eu estudasse, passaria', o verbo indica:",
        "opcao": ["A)certeza", "B)condição", "C)ordem", "D)sorte"],
        "correta": "B"
        },
    {
        "matéria": "Português",
        "pergunta": "A palavra 'porquê' é usada como:",
        "opcao": ["A)preposição", "B)conjução", "C)substantivo", "D)advérbio"],
        "correta": "C"
        },
    {
        "matéria": "Português",
        "pergunta": "Em 'Os alunos chegaram atrasados', 'atrasados' é:",
        "opcao": ["A)adjetivo", "B)advérbio", "C)substantivo", "D)preposição"],
        "correta": "A"
        },
    {
        "matéria": "Português",
        "pergunta": "Qual a frase correta?",
        "opcao": ["A)Houve muitos problemas", "B)Haviam ocorrido erros", "C)Haviam muitas pessoas", "D)Houveram muitos prooblemas"],
        "correta": "A"
        },
    {
        "matéria": "Português",
        "pergunta": "O sujeito em “Choveu muito ontem” é",
        "opcao": ["A)oculto", "B)simples", "C)inexistente", "D)composto"],
        "correta": "C"
        },
    {
        "matéria": "Português",
        "pergunta": "Em 'Ele não só estudou, mas também trabalhou', temos:",
        "opcao": ["A)explicação", "B)oposição", "C)comparação", "D)adição"],
        "correta": "D"
        },
    {
        "matéria": "Português",
        "pergunta": "A função da vírgula em 'João, venha aqui' é:",
        "opcao": ["A)separa enumeração", "B)indicar tempo", "C)separar o sujeito", "D)indicar vocativo"],
        "correta": "D"
        }

]


def gerar_simulado(quantidade_de_questoes):

    questoes_sorteadas = random.sample(banco_de_questoes, 10)
    return questoes_sorteadas


async def rodar_simulado(ctx, bot):
    acertos = 0
    erros = 0
    questoes_do_teste = gerar_simulado(10)

    await ctx.send("=== INÍCIO DO SIMULADO ===")

    for numero, questao in enumerate(questoes_do_teste, 1):
        # Montando o texto da questão
        texto_questao = f"\n**Questão {numero} — {questao['matéria']}**\n"
        texto_questao += f"{questao['pergunta']}\n"
        for alternativa in questao["opcao"]:
            texto_questao += f"{alternativa}\n"
            
        await ctx.send(texto_questao)
        
        # Função interna para verificar se a mensagem veio da mesma pessoa e canal
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        # O bot vai esperar aqui até receber uma mensagem (sem limite de tempo)
        msg = await bot.wait_for('message', check=check)
        resposta = msg.content.strip().upper()
        
        if resposta == questao["correta"]:
            acertos += 1
            await ctx.send("✅ *Resposta correta!*")
        else:
            erros += 1
            await ctx.send(f"❌ *Resposta errada.* A alternativa correta era a **{questao['correta']}**")
            
        await ctx.send("----------------------------------------")
        
    await ctx.send("\n=== **FIM DO SIMULADO** ===")
    await ctx.send(f"🏆 Você acertou **{acertos}** questões e errou **{erros}**!!!")