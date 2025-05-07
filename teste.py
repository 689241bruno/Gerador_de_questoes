
import google.generativeai as genai

print("_________________________________________")
print("           GERADOR DE QUESTÕES           ")
print("_________________________________________")

genai.configure(api_key="AIzaSyBtcwKVWxeoe9lIP2ClrezFO-jV0k8gzYY")
model = genai.GenerativeModel("gemini-pro")

questao = input(str('Digite sua questão aqui: '))
prompt = 'Faça uma outra questão semelhante com nessa (com números de linha e raciocíneo lógico parecidos) IMPORTANTE não dar a resposta de nenhuma das duas questões e também não precisa me mostrar a linha de raciocíneo ' + questao
resposta = model.generate_content(prompt)
print("_________________________________________")
print('Sua questão: ')
print(resposta.text)
print("_________________________________________")
print('')
print('')
print('')

 
 
