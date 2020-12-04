using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Teste
{
    class Calculadora
    {
        static void Main(string[] args) 
        {   
            //simples calculadora
            
            double n1, n2;
            
            string tmp;
            
            Console.WriteLine("Digite um número: ");
            tmp = Console.ReadLine();
            n1 = int.Parse(tmp);
            
            Console.WriteLine("Digite mais um número: ");
            Console.ReadLine();
            n2 = int.Parse(tmp);
            
            double resultado;
            
            //soma e mostra o resultado na tela
            resultado = n1 + n2;
            Console.WriteLine("O resultado da soma é :" + resultado);
            
            //subtrai e mostra o resultado na tela
            resultado = n1 - n2;
            Console.WriteLine("O resultado da subtração é: " + resultado);
            
            //multiplica e mostra o resultado na tela 
            resultado = n1 * n2;
            Console.WriteLine("O resultado da multiplicação é: " + resultado);
            
            //divide e mostra o resultado na tela
            resultado = n1 / n2;
            Console.WriteLine("O resultado da divisão é:" + resultado);
    }
  }
}	