using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using UnityEngine.UI;
using System.IO;

public class BasicSyntax : MonoBehaviour {

    private string output;
    public GameObject txtOutput;
    public GameObject txtInput;

  

    public void onClick(){

        
        
        //basic math
        float x = 3.14f;
        float y = 2.82f;

        float sum = x + y;
        float diff = x - y;
        float prod = x * y;
        float quotient1 = x / y;

        int quot_int = 7 / 4;
        int remainder = 7 % 4;

        output = "";
        output += "Sum: " + sum + "\n";
        output += "Differenece: " + diff + "\n";
        output += "Product: " + prod + "\n";
        output += "Quotient: " + quotient1 + "\n";
        output += "Integer Quotient: " + quot_int + "\n";
        output += "Integer Remainder: " + remainder + "\n";


        //input field
        // output = "";
        // string input = txtInput.GetComponent<InputField>().text;
        // output = "Hello there " + input;


        //selection structure
        output = "";
        int m = 13;
        int n = 14;
        int k = 5;

        // && is and, || is or (a single one is bitwise)
        if(m < n && m < k){
            output = "m is smaller";
        }
        else if(n < m && n < k){
            output = "n is the smallest number";
        }
        else{
            output = "it looks like k is smaller";
        }


        //loops
        output = "";
        int counter = 0;
        while(counter < 11){
            output += "the number is growing, it's at " + counter + "\n";
            counter++;
        }


        //lists and for loops
        output = "";
        List<int> numbers = new List<int>();
        numbers.Add(9);
        numbers.Add(3);
        numbers.Add(14);


        for(int i=0; i < numbers.Count; i++){
            output += numbers[i] + ", ";
        }
        output += "\n";

        List<string> names = new List<string>();
        names.Add("Bob");
        names.Add("Sally");
        names.Add("Becky");

        for(int name = 0; name < names.Count; name++){
            output += names[name] + ", ";
        }


        //write a text file
        output = "";
        string forFile = "Here is a string to write to a text file";
        File.WriteAllText("sample.txt", forFile);



        output = File.ReadAllText("sample.txt");


        txtOutput.GetComponent<Text>().text = output;

    }//end onClick()

}//end class
