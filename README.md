#  **Criptografias em python**

### **Técnicas clássicas de encriptação:**
Para aplicações básicas da criptografia em suas diversas áreas como em softwares, circuitos integrados, sites etc.
Utilizando criptografias simétricas e também de chave pública, ou assimétricas.

Os códigos seguem a seguinte ordem:

### **1. [Cifra de César aleatória e Cifras monoalfabéticas aleatórias](https://github.com/erickcharlesneves/Cripto/commit/ba24c1e11bad2f75e6d6d33b6c4d69e861745126#commitcomment-142550589);**

**Contextualização sobre:**
O uso mais antigo que conhecemos de uma cifra de substituição, e o mais simples, foi feito por Júlio César. A cifra de César envolve substituir cada letra do alfabeto por aquela que fica três posições adiante.
Por exemplo,

```sql
claro: a b c d e f g h i j k l m n o p q r s t u v w x y z
cifra: D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
```

Ainda se atribuirmos um equivalente numérico a cada letra em ordem:

```sql
a b c d e f  g h  i  j   k    l   m
0 1 2 3 4 5  6 7  8  9   10   11  12
n   o   p   q   r    s    t    u    v   w   x   y   z
13  14 15   16  17   18   19   20   21  22  23  24  25
```

Ainda se atribuirmos um equivalente numérico a cada letra em ordem:

```sql
a b c d e f  g h  i  j   k    l   m
0 1 2 3 4 5  6 7  8  9   10   11  12
n    o   p   q   r    s    t    u    v   w   x   y   z
13   14  15  16  17   18   19   20   21  22  23  24  25
```

Trata-se de uma criptografia facilmente quebrável por uma criptoanálise por força bruta. 
Pois os algoritmos de encriptação e decriptação são conhecidos, existem apenas 25 chaves para experimentar, a linguagem do texto claro é conhecida e facilmente reconhecível.

**Porém no código upado “cifragemcesar_aleatoria” dificultei um pouco mais ao fornecer uma régua de caracteres maior para a encriptação da mensagem, permitindo assim uma substituição aleatória.**

Se, em vez disso, a linha “cifra/regua_caracteres” puder ser qualquer permutação dos 26 caracteres alfabéticos, então haverá 26! ou mais do que 4 × 10^26 chaves possíveis. Isso significa 10 ordens de grandeza a mais do que o espaço de chave para DES, e evitaria qualquer técnica de força bruta para criptoanálise. Essa técnica é conhecida como cifra por substituição monoalfabética, pois um único alfabeto de cifra (mapeando do alfabeto claro para um cifrado) é utilizado por mensagem.

**Em seguida nos dois outros códigos upados “cifragem_msn” e “decifragem_msn” faremos a encriptação e decriptação, respectivamente, da mensagem por uma cifra monoalfabética por substituição aleatória.** 

Porém ainda existe uma outra linha de ataque que torna as cifras monoalfabéticas fáceis de se quebrar caso o criptoanalista conheça, porque refletem os dados de frequência do alfabeto original. Uma contramedida é oferecer vários substitutos, conhecidos como homófonos, para uma única letra.
Por exemplo, a letra e poderia ser atribuída a diversos símbolos de cifra diferentes, como 16, 74, 35 e 21, com cada homófono usado em rodízio, ou aleatoriamente. Se o número de símbolos atribuídos a cada letra for proporcional à frequência relativa dela, então a informação de frequência de única letra é completamente extinta.

O grande matemático Carl Friedrich Gauss acreditava ter criado uma cifra indecifrável usando homófonos.
Porém, até mesmo com homófonos, cada elemento do texto claro afeta somente um elemento do texto cifrado, e padrões de múltiplas letras (por exemplo, frequências de digrama) ainda sobrevivem no texto cifrado, tornando a criptoanálise possível.

Dois métodos principais são usados nas cifras de substituição para reduzir a extensão da estrutura sobrevivente do texto claro no cifrado. Uma técnica é encriptar várias letras do texto claro **(Cifra de Hill códigos upados conforme item 2 abaixo)**, e a outra é usar vários alfabetos de cifra **(Cifra de Vigenère (poli alfabética) conforme item 3, abaixo)**. 


###  2. [Cifra de Hill(1ª)](https://github.com/erickcharlesneves/Cripto/commit/ca583b3e712109b8d3db8b00639fce2cabb20886#commitcomment-142653992) - [Cifra de Hill(2ª)](https://github.com/erickcharlesneves/Cripto/commit/48fa4080543a8cdff130092721e5c256d1a67c87#commitcomment-142550069);
###  3. [Cifra de Vigenère](https://github.com/erickcharlesneves/Cripto/commit/3d123c520bb734d2676b919a13f7287d64c51875#commitcomment-142549762);
###  4. [AES](https://github.com/erickcharlesneves/Cripto/commit/7ab832858ff0781de03f420168b0eaa083cf1969#commitcomment-142625749)(Advanced Encryption Standard) simplificado. (Necessário instalar bibliotecas: cryptography, pycryptodome, pycrypto ou execução em sage math);

