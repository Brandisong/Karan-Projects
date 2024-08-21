// Pi to Nth Number
// User inputs a number, and that many digits of pi are printed
// Prints up to a hundred digits

// Pi is stored as a string, as it's too big for number types
const string PI = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679";

// Get and parse input
Console.WriteLine("Please input n (number of decimal places)");
string inputString = Console.ReadLine() ?? "0";

int numberOfDigits;
if (Int32.TryParse(inputString, out numberOfDigits))
{
    // Reduce to 100 digits if input is > 100
    if (numberOfDigits > 100)
    {
        numberOfDigits = 100;
    }

    // Successfully parsed, print pi to n digits
    // Adds two characters for the "3." prefix
    Console.WriteLine(PI.Substring(0, numberOfDigits + 2));
}
else
{
    Console.WriteLine("Error: failed to parse, please enter an integer");
}