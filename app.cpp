#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <direct.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <vector>
#include <limits>
#include <algorithm>


// use of preprocessor used only to debug
#define DEBUG             //uncomment for debugging on


// Program name: app.cpp  By: Stan S.  11-16-2014  v.1
//
// Purpose: Installer ...
//
// Usage  : g++ -Wall -std=c++11 app.cpp
//
// Description:
//
//        Note:  ~2GB Installer max size
//               http://superuser.com/a/667614
//               For larger size, additional files, archives required.

// just coded, feature: can have spaces in the return type  11-27-2014
// currently, todo: to update how the function defintion signature are detected
// note: change the last line in the to_code_block  function to return data; from return truncate (data , 3);  // used to code and test (used for just a few line of the converted base64 zip files appended to the source code file)  

using namespace std;

class splitstring : public string {
    vector<string> flds;            //private by default
public:
    splitstring(char *s) : string(s) { };
    vector<string>& split(char delim, unsigned int rep=0);
};

// data bundling, perhaps some methods to shape its data contents
class back_pack {

public:
	vector<string> type, name, args;

	back_pack() {}
	back_pack(vector<string> a, vector<string> b, vector<string> c):type(a),name(b),args(c) {}
	print_size(){ cout << this->type.size() << " " << this->name.size() << " " << this->args.size() << " " << endl; return 0;}
	add(string t, string u, string v) { this->type.push_back(t); this->name.push_back(u); this->args.push_back(v);  return 0;}
	print_all(){ int i=0; for ( auto &item : this->type) { cout << this->type[i] << " " << this->name[i] << " " << endl; i++;} return 0; }
};

// note:   when  a function   changes a           datatype       to a constant reference 
//                                e.g.,     const datatype &

// The FIX:  is that   small tests (unit tests) have shown  must  put keyword  const  after method name of class and after its open,close parentheses
// this will resolve the following error message something like:
// error: passing ‘const …'’ as ‘this’ argument of ‘…’ discards qualifiers     http://stackoverflow.com/a/19074059
// Note: this warning will prevent the compiler (from) to create the binary, i.e., it will not compile until the fix is applied

typedef unsigned long long MAX_LENGTH;

typedef signed long long size_find;   // not size_t  that converts -1 to some integer

const unsigned long long max_length_check = std::numeric_limits<unsigned long long>::max();


string base64_encode(unsigned char const* , unsigned int len);   /* base64.h */
string base64_decode(string const& s);                           /* base64.h */


string ReplaceString(string, const string& , const string& );  // not using, just for example
void ReplaceStringInPlace(string& , const string& , const string& );


// sort of an idea or not: if pseudo-keywords were used, say:
// LOCK   =    const   variable  &       e.g.,        LOCK variable
// EDIT   =    &                         e.g.,        EDIT variable

// perhaps something like:
typedef const  &   LOCK;  // http://stackoverflow.com/a/1035803
typedef        &   EDIT;
//typedef          COPY;  // ( redundant, moot ) that is pass by value (by copy) by c++ by default
 
 
// Just some notes: 
// Aside from the Installer... wanted a feature of optimization (for this and perhaps other projects)
// Because Pass by Value is cleaner code in c++ (without all the const&) wanted that, e.g., python, but wanted the speed and the safe passing by constant reference feature
// Therefore created a perhaps innovative auto generated const &, constant reference feature, to the function arguments
// The code between the tags    BEGIN Prototypes to const
//                       and    END   Prototypes to const   is modified with a speed_up algorithm.
//
// 1.Not dealing with, the code is not written for variables intended to be passed by value (just manually edit to preference)
//   Though there is an example of how code might use a function that intends pass by value but gets passed by constant reference (useful or not based on preference)
// 2.Not dealing with function defintion signature that's using the default parameter feature
// Anyway, the speed up algorithm depends on function prototypes on a single line that are betwen the BEGIN and END tags
//
// Speed_up description:
// The speed up algorithm simply puts   const   and   &  around an argument  ( that does not already have an & ) in the prototype and definition header
// Sidenote: Comments are helpful even when developing this, there are moments asking what's going on again, how does this work again, 
//           how are the tags used, ect., that the comments explain explicitly


/* Note: The function prototypes between the following BEGIN and END comment tags are edited automatically by the speed_up algorithm when first running this compiled source code program */
// The source code file in the  code_file  variable is modified


/* NOTE: updated: speed_up_prototypes can now have spaces in the return type  */
//       final: single line comments on one line only, with // or /* */ can be used between tags

/* BEGIN Prototypes to const and & */

string         to_code_block( string );
int            to_file(    string, string );                   // binary mode,  "\n" to linefeed only  \n

int            to_file_text( string, string );                 // text mode,    "\n" to carriage return and linefeed  \r\n
MAX_LENGTH     to_file_append( string, string );               // or just   size_t

string         get_file( string );
vector<string> get_lines( string );

vector <string> & get_source_code ( string , vector<string> & );

string         speed_up_prototypes( string, string, vector<string> , back_pack & );  
string         speed_up_fds(string, vector<string>, back_pack ); // speed_up_definition_signatures

string         uncomment_by_begin_end( string, string, vector<string> );

string         add_prototypes( string, vector<string>, vector<string> );

string         create_foo( string, string, vector<string>, vector<string> & );  // create_get_binary_base64_function

bool           is_fds( string, back_pack ); // is_function_definition_signature
bool           contains_vector_data_in_line(string, vector<string>);

bool           findit( string, vector<string> );
bool           findprototype( vector<string> , vector<string> );
bool           exists( string );
bool           contains( string, string );

string         trim( string );                          // php like trim
size_find      strpos ( string, string, size_t );       // php like strpos, but returns -1 like find if not found
string         squeeze( string );                       // removes spaces

int            test();               // to remove

int            test_const_ref( back_pack );


string         wrapit (string);  // this creates the constant reference for each function definition signature argument that does not already have an &

string         truncate(string, int);  // used to code, test this program // truncates data appended to source code file
  
/* END Prototypes to const and & */



/* Note: The function prototypes will automatically be created between the following BEGIN and END comment tags when first running this compiled source code program */
// The source code file in the  code_file  variable is also modified

/* BEGIN Auto-Generated Prototypes */ 

/* END Auto-Generated Prototypes */



int main() {


vector<string> source_code;

// on second compile, the next two uncommented statement lines are changed
// change this to whatever e.g.,    done.whatever.txt
const string code_file = "test.txt.cpp"; // to modify itself, set to the source code filename "app.cpp"
// change this to the source code filename to   the output filename  that's created by running the program the first time with the initial source code
source_code = get_source_code( "app.cpp", source_code); // to modify itself, set to code_file


to_file_text(code_file, uncomment_by_begin_end( "/* BEGIN Unzip */" , "/* END Unzip */" , source_code ));
source_code = get_source_code( code_file, source_code);

cout << "Creating filename: " << code_file << endl;


back_pack prototype_data;  // for functions speed_up info


to_file_text(code_file, speed_up_prototypes("/* BEGIN Prototypes to const and & */" , "/* END Prototypes to const and & */" , source_code , prototype_data ) );
source_code = get_source_code( code_file, source_code);


//prototype_data.print_size();         // perhaps modify additional   back_pack   contents 
//prototype_data.modify();  // contents , perhaps whatever
//prototype_data.print_all();


to_file_text(code_file, speed_up_fds( "/* END MAIN Function */" , source_code , prototype_data ) );
source_code = get_source_code( code_file, source_code);

// to remove
// to test the  error-warning message about an object (of a class) passed as constant references and then running one of its methods
test_const_ref( prototype_data );



std::vector<MAX_LENGTH>  r;   // to review results
std::vector<string>      p;   // contains the prototypes to add the Auto-Generated function prototypes Area

// files to convert to base64 should be in the same directory as this program
                    //  should rename to create_foo  to  create_get_binary_base64_function
r.push_back( to_file_append( code_file, create_foo( "php", "unzip.php"     , source_code, p )));
r.push_back( to_file_append( code_file, create_foo( "exe", "php.exe"	   , source_code, p )));
r.push_back( to_file_append( code_file, create_foo( "dll", "php5ts.dll"    , source_code, p )));
r.push_back( to_file_append( code_file, create_foo( "zip", "my-archive.zip", source_code, p )));
source_code = get_source_code( code_file, source_code);



// TEST PROTOTYPES
//cout << "Function Prototype length:" << p.size() << endl;
//for ( auto& item : p ) {
//	cout << "Prototype: " << item << endl;
//}


	
to_file_text ( code_file, add_prototypes( "/* BEGIN Auto-Generated Prototypes */" , source_code , p ) );
//  if going to edit source code again, update source code with:   source_code = get_source_code( code_file, source_code);


bool refresh = false;

for ( auto &val : r ) {
	cout << "Length appended is:" << val << endl;
	
	if (val > 0) {
		refresh = true;
	}
}

if (refresh) {
	printf("Need to refresh source code and compile, early exit of program");
	exit (1);
}


/* Note: The following BEGIN and END Unzip tags are used to automatically uncomment the statements between the tags */
// LEAVE the statements between the BEGIN and END Unzip tags COMMENTED OUT with // ONLY       NOT the /* type comment lines */
/* the program automatically uncomments these lines in the source code file in the  code_file  variable when first running this compiled source code program */

/* BEGIN Unzip */

//to_file( "unzip.php"     ,  base64_decode( get_binary_php() )); // the get_binary_ ... functions are auto generated at first run 
//to_file( "php.exe"       ,  base64_decode( get_binary_exe() )); // because these functions do not exist yet
//to_file( "php5ts.dll"    ,  base64_decode( get_binary_dll() )); // at first run, these need to be commented out
//to_file( "my-archive.zip",  base64_decode( get_binary_zip() )); // and any lines betweeen "BEGIN Unzip" and "END Unzip" that comment lines are uncommented

/* END Unzip */



// WORKING ON  HERE ...


system("php.exe unzip.php");

// check for the uncompressed python binary program compiled by py2exe

// something like
//        system("dist/python_binary.exe");

// the intended binary to execute  that the Installer is installing.
system("run.exe");

// it unzips to same directory as the Installer
// once unziped, then ...


// does the Install ask for an install directory
// if it does, perhaps move files there and run 

return 0;
}

/* BEGIN MAIN Function */
/* Do not delete the following END main tag (not using the BEGIN main tag for now) the code AFTER the END main tag is searched by the function speed_up_fds to find the function definition signatures */
/* END MAIN Function */

int
test() {
	return 0;
}


int test_const_ref( back_pack s) {
	// this should invoke the    const  ref   warning, that stops the compiler from creating the binary
	s.print_all();
return 0;
}

string 
to_code_block(string text) { // By: Stan Switaj

	MAX_LENGTH size = text.length();
	cout << "Length is:"   << size << endl;
	cout << "Max size is:" << max_length_check << endl;

	if (size > max_length_check) {
			printf("Error archive size overflow, early exit of program");
			exit (1);
	}

	int line_length_every_nth = 80;

	string data = "\n"; // nice, start it with a newline
	string line;
	for (MAX_LENGTH i = 0; i < size; i++) {

		if ((i % line_length_every_nth) == 0) { // happens at 0, and at every nth thereafter
		
			line += "\"";         // an ending quote  // codepoint HERE #1
			line += "\n";         // done with line   // codepoint HERE #1
			data += line;
		}

		if ((i % line_length_every_nth) == 0) { 
		
			line = "";            // starts a line
			line += "\"";         // a starting quote
		}
		
		line += text[i];
	}
	
	data += line + "\"" + "\n";
    data = data.substr(2,data.length());    // removes the quote and newline from codepoint HERE #1 point                             	
	
#ifdef DEBUG
	return truncate (data , 3);    // data;  // remove truncate   for TESTING, etc.
#else
	return data;
#endif
}

// function_suffix should be unique, not checking in this program
string 
create_foo(string function_suffix, string file, vector<string> source_code, vector<string> &v) { // create_get_binary_base64_function

    if ( findit( "string get_binary_" + function_suffix + "() {" , source_code ) )
    return "";
    
    if ( exists(file) == false) {
    	cout << "Will not append to source code, because File does not exist, to create a base64 function returning a multiline string variable, \n";
		cout << "Perhaps already distributed ( i.e., already sent to clients' machines for install )" << endl;
    return "";
    }
    
    string var;
    string data;      // contains file
    string base64;    // contains base64 of file
    string contents;  // contains multiline string ( of base64 of file )
    data = get_file( file );
    base64 = base64_encode( reinterpret_cast<const unsigned char*>( data.c_str() ), data.length() );
    contents = to_code_block ( base64 );
    var +=  "string get_binary_" + function_suffix + "() {\n";
v.push_back("string get_binary_" + function_suffix + "() ;  ");
    var +=  "string data = " + contents + ";\n";
    var +=  "return data;\n}\n";
    return "\n" + var;

}

string 
add_prototypes( string line, vector<string> source_code, vector<string> prototypes ) {
	
	if ( findprototype( source_code , prototypes ) )
	return "";
	
	string out;
	
	for ( auto &item : source_code ) {
		
		if ( trim(item) == line ) {
		
			out += item + "\n";
			
			for (auto &it : prototypes) {
				out += it + "\n";
			}
		}
		else {
			out += item + "\n";
		}
	}

return out;
}

bool 
contains(string line, string sub) {
	return  line.find(sub) != string::npos  ? true : false;		
}

bool 
contains_vector_data_in_line(string line, vector<string> v) {
	bool find = false;
	for ( auto &item: v) {                           
		if (line.find(item) != string::npos) { 
			//cout << "Found:" + item << endl;         
			return true;
		}
	}
	return find;
}

bool 
is_fds( string line, back_pack data ) { // is_function_definition_signature
	
	bool find = false;
	
	// the following I define as a function definition signature with 4 pieces of data,information
	
	/* the line must contain only one (
	   the line must contain a function name captured in the back_pack from the prototypes
	   the line cannot contain a ;
	   the line cannot contain a =   (for now, this version excludes  any fds that has uses the default paramater feature (due to the = sign)
        (possible for next version, todo: to check the return type in addition to the function name, why, so that the fds could contain a = sign, i.e., can deal with a fds with default paramater(s) )
	*/
	
	
	size_t n = std::count(line.begin(), line.end(), '(');
	
	if (n == 1 && contains_vector_data_in_line(line, data.name) && 
	(false == contains(line, ";")) && (false == contains(line, "="))  ) {
		return true;
	}

	return find;
}

// not using, but pass by value example function minor fix   with speed_up  compatibility
string 
ReplaceString(string subject, const string& search, const string& replace) {
    string sub = subject; // by value compatibility, a manual copy, with speed_up approach
	size_t pos = 0;
    while ((pos = sub.find(search, pos)) != string::npos) {
         sub.replace(pos, search.length(), replace);
         pos += replace.length();
    }
    return sub;
}

void 
ReplaceStringInPlace(string& subject, const string& search, const string& replace) { // http://stackoverflow.com/a/14678911
    size_t pos = 0;
    while ((pos = subject.find(search, pos)) != string::npos) {
         subject.replace(pos, search.length(), replace);
         pos += replace.length();
    }
}

// speed_up_function_definition_signatures
// end_comment_of_main_function
// fds = function definition signature
string 
speed_up_fds( string end, vector<string> source_code , back_pack data ) {  //11-24-2014

//part 2 - edit function definition signatures



// HERE...



	bool start = false;
	string out = "";
	string trimline = "";
	string trimtrail = "";      // for a potential additional check to find a fds, not used for now, currently just using function name for find,search
                                    // for coding styles that optionally,sometimes trail their return data type on the previous line from the fsd
								
	// for now, just after end main tag in comments :   e.g.,    /* END MAIN Function */
	
	int i = 0;
	for ( auto &line : source_code )
	{
		trimline = line;
		
		if (i == 0) {
			out += trimline + "\n";
			trimtrail = trimline;
			i++;
			continue;
		}
		
		if ( trimline == end )
		start = true;
		
		
		if (trimline.length() >= 2) {
			if (trimline.substr(0,2) == "//" || trimline.substr(0,2) == "/*") { // skips commented out lines (not comment blocks for now)
				out += trimline + "\n";
				trimtrail = trimline;
				i++; 
				continue;
			}
		}		
		
		
		if (start)
		{
			if ( is_fds(trimline, data)	) 
			{
				ReplaceStringInPlace( trimline, "(", " ( ");
				ReplaceStringInPlace( trimline, ")", " ) ");
				ReplaceStringInPlace( trimline, ",", " , ");
				ReplaceStringInPlace( trimline, "{", " { ");
				ReplaceStringInPlace( trimline, "//", " // ");
				ReplaceStringInPlace( trimline, "/*", " /* ");
				ReplaceStringInPlace( trimline, "*/", " */ ");
				
					string pre  = "";
					string args = "";
					string post = "";
					
					bool start = true;
					bool mid   = false;
					bool rest  = false;	
					
					splitstring s( (char *) trimline.c_str() );   
					vector<string> 	flds = s.split(' ');

					for ( auto &item : flds )
					{
							if ( item == "/" || item == ")" ) {
								mid = false;
								rest = true;
								start = false;
							}
                                                                                // note: no { } around ifs
							if (start)
							pre  += item + ' ';

							if (mid)
							args += item + ' ';
							
							if (rest)
							post += item + ' ';
								
							if ( item == "(" ) {
								start = false;
								mid = true;
							}											
					}
				
				
				string center = "";
				
				splitstring m( (char *) args.c_str() );   
				vector<string> vars = m.split(',');
				
				for ( auto &item : vars ) 
				{
					if (contains(item, "&") )
						center += item + ", ";
					else                        
						center += wrapit( item )  + ", " ; // wraps  datatype  with   const  and  & 
				}
							
				if (center.length() >= 2)
				center = center.substr(0,center.length() - 2);
				
				
				trimline =  pre + center + " " + post + "\n";  // can optionally trim pre and remove space immediate space after (
			}
		}
		
	out += trimline + "\n";

	trimtrail = trimline;
	i++;
	}
	
	return out;
}

string
wrapit (string s ) {

	string out = "";
	
	splitstring w( (char *) s.c_str() );   
	vector<string> 	flds = w.split(' ');

	if ( flds.empty() )
	return "";
	
	
	out += "const ";
	
	for ( auto & item : flds )
	{
		if (flds.back() != item)
		out += item + ' ';
	}
	
	out += "& " + flds.back();
	
	return out;
}

string 
speed_up_prototypes( string start, string end, vector<string> source_code, back_pack &data ) {

//part 1 - edit function prototypes

	string out = "";
	bool speed_increase = false;

	for ( auto &line : source_code )
	{
		if (start == line) {
			speed_increase = true; // from start line
			out += line + "\n";
			continue;
		}
	
		if (end == line) {
			speed_increase = false; // to end line
			out += line + "\n";
			continue;
		}	
		
		string return_type = "";
		string function_name = "";
		string trimline = "";
		string front = "";
		string arguments = "";
		string mid = "";          // processed arguments variable
		string rest = "";
		
		if (speed_increase) 
		{
			trimline = trim(line);
			
			if (trimline == "") {
				out += "\n";
				continue;
			}		
			
			if (trimline.length() >= 2) {
				if (trimline.substr(0,2) == "//" || trimline.substr(0,2) == "/*") { // comment lines
					out += trimline + "\n";  
					continue;
				}
			}
			
			ReplaceStringInPlace( trimline, "(", " ( ");
			ReplaceStringInPlace( trimline, ")", " ) ");
			ReplaceStringInPlace( trimline, ";", " ; ");
			
			// part  #1
			//update #1, return type with spaces
			string str = "";
			if ( contains (trimline, "(") ) {
					str = trimline.substr(0,   strpos( trimline, "(", 0)   );
					
					cout << "Substring is: " << str << endl;
				
					splitstring b( (char *) str.c_str() );   
					vector<string> type_name = b.split(' ');	
					
					for ( auto& item : type_name)
					{
						if (type_name.back() == item)
							function_name = item;
						else
							return_type += item + ' ';
					}
					
				cout << "Return Type:" << return_type << endl;
				cout << "Function Name:" << function_name << endl;					
			}
			//done update #1, return type with spaces
			
			
			bool args = false;
			bool end = false;			
			
			splitstring s( (char *) trimline.c_str() );   
			vector<string> 	flds = s.split(' ');
			

			
			int i = 0;
			for ( auto &item : flds ) // would also have an enumerate i variable feature here if C++ had this feature
			{
				//if ( i == 0)
				//return_type = item;
				
				//if ( i == 1)
				//function_name = item;
			
				if (item == ")") {
					end = true;
					args = false;
				}
				
				if (end == true) {
					rest += item + " ";
					continue;
				}
				
				if (args == true) {
					arguments += item + " ";
					continue;
				}
				
				if (item == "(")
				args = true;
				
				
				front += item + " ";
				i++;
			}
			
			
			splitstring m( (char *) arguments.c_str() );   
			vector<string> vars = m.split(',');			
			
			for ( auto &item : vars ) 
			{
				if ( contains(item, "&") )
					mid += trim(item) + " , ";                       // can remove space before comma just an extra end space
				else
					mid += "const " + trim(item) + " & " + ", ";     // can remove immediate space after &  just an extra end space
			}
			
			
			if (vars.size() > 0)                          // minor adjustment
			mid = mid.substr(0,mid.length() - 2);         // to remove comma and space

			
			out += front + mid + rest + "\n";             // can optionally trim front to remove space after (
		}
		else {
			out += line + "\n";
		}
		
		
		if (function_name != "")
		data.add(return_type, function_name, arguments);
	}
	
	return out;
}

string 
uncomment_by_begin_end( string start, string end, vector<string> source_code ) {

	string out = "";
	string trimline = "";
	bool uncommenton = false;

	for ( auto &line : source_code ) {

		if (start == line)
		uncommenton = true; // start uncomment
		
		if (uncommenton == true) {
		
			if (line.length() >= 2) {
			
				trimline = trim(line);
				
				if (trimline.substr(0,2) == "//" )
				line = trimline.substr( 2 , trimline.length() ) ;
			}
		}

		out += line + "\n";
		
		if (end == line)
		uncommenton = false; // end uncomment
	}
	return out;
}

int 
to_file(string file, string content) {
	
	ofstream fp;
	fp.open ( file, ios::binary | ios::out );
	fp << content;
	fp.close();
	return 0;
}

int 
to_file_text(string file, string content) { // http://stackoverflow.com/a/229971

	ofstream fp( file , ios::out );
	fp << content;
	fp.close();
	return 0;
}

MAX_LENGTH 
to_file_append(string file, string content) {

	ofstream fp(file , ios::app);
	fp << content;
	fp.close();
	return content.length();
}

string 
get_file(string file) {

	ifstream fp;
	fp.open( file, ios::in | ios::binary );
	string contents(  (istreambuf_iterator<char>(fp)), istreambuf_iterator<char>()  );
	fp.close();
	return contents;
}

vector<string> & 
get_source_code( string source_file, vector<string> & source_code ) { // just to try with a return type by ref

	if (!source_code.empty())
	source_code.clear();

	source_code = get_lines( source_file );
	return source_code;
}

vector<string> 
get_lines(string file) {

	vector<string> elems;

	std::ifstream filein(file);

	for (std::string line; std::getline(filein, line); ) {
		elems.push_back (line);
	}

	return elems;	
}

string
truncate(string data, int n) {   // truncate_string_by_line

	string out = "";
	
	std::istringstream ss(data);  //stringstream ss(s);
	
	int i = 0;
	
	if ( n > 0)
		for (std::string line; std::getline( ss , line); ) {
		
			out += line + "\n";
			
			if ( i == n)
			break;
			
			i++;
		}
	
	return out;
}

bool 
findit( string item , vector<string> multilines ) {

	for ( auto &line : multilines ) {
	
		if (item == line)
		return true;
	}
	
	return false;
}

bool 
findprototype( vector<string> source_code, vector<string> prototypes) {

	for ( auto &line : prototypes ) {
		
		if ( findit ( line , source_code ) )
		return true;
	}
	
	return false;
}

bool 
exists(string file) {
	return std::ifstream(file).good(); // http://stackoverflow.com/a/24750132
}

/* begin base64.cpp */
static const std::string base64_chars = 
             "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
             "abcdefghijklmnopqrstuvwxyz"
             "0123456789+/";


static inline bool is_base64(unsigned char c) {
  return (isalnum(c) || (c == '+') || (c == '/'));
}

std::string base64_encode(unsigned char const* bytes_to_encode, unsigned int in_len) {
  std::string ret;
  int i = 0;
  int j = 0;
  unsigned char char_array_3[3];
  unsigned char char_array_4[4];

  while (in_len--) {
    char_array_3[i++] = *(bytes_to_encode++);
    if (i == 3) {
      char_array_4[0] = (char_array_3[0] & 0xfc) >> 2;
      char_array_4[1] = ((char_array_3[0] & 0x03) << 4) + ((char_array_3[1] & 0xf0) >> 4);
      char_array_4[2] = ((char_array_3[1] & 0x0f) << 2) + ((char_array_3[2] & 0xc0) >> 6);
      char_array_4[3] = char_array_3[2] & 0x3f;

      for(i = 0; (i <4) ; i++)
        ret += base64_chars[char_array_4[i]];
      i = 0;
    }
  }

  if (i)
  {
    for(j = i; j < 3; j++)
      char_array_3[j] = '\0';

    char_array_4[0] = (char_array_3[0] & 0xfc) >> 2;
    char_array_4[1] = ((char_array_3[0] & 0x03) << 4) + ((char_array_3[1] & 0xf0) >> 4);
    char_array_4[2] = ((char_array_3[1] & 0x0f) << 2) + ((char_array_3[2] & 0xc0) >> 6);
    char_array_4[3] = char_array_3[2] & 0x3f;

    for (j = 0; (j < i + 1); j++)
      ret += base64_chars[char_array_4[j]];

    while((i++ < 3))
      ret += '=';

  }

  return ret;

}

std::string base64_decode(std::string const& encoded_string) {
  int in_len = encoded_string.size();
  int i = 0;
  int j = 0;
  int in_ = 0;
  unsigned char char_array_4[4], char_array_3[3];
  std::string ret;

  while (in_len-- && ( encoded_string[in_] != '=') && is_base64(encoded_string[in_])) {
    char_array_4[i++] = encoded_string[in_]; in_++;
    if (i ==4) {
      for (i = 0; i <4; i++)
        char_array_4[i] = base64_chars.find(char_array_4[i]);

      char_array_3[0] = (char_array_4[0] << 2) + ((char_array_4[1] & 0x30) >> 4);
      char_array_3[1] = ((char_array_4[1] & 0xf) << 4) + ((char_array_4[2] & 0x3c) >> 2);
      char_array_3[2] = ((char_array_4[2] & 0x3) << 6) + char_array_4[3];

      for (i = 0; (i < 3); i++)
        ret += char_array_3[i];
      i = 0;
    }
  }

  if (i) {
    for (j = i; j <4; j++)
      char_array_4[j] = 0;

    for (j = 0; j <4; j++)
      char_array_4[j] = base64_chars.find(char_array_4[j]);

    char_array_3[0] = (char_array_4[0] << 2) + ((char_array_4[1] & 0x30) >> 4);
    char_array_3[1] = ((char_array_4[1] & 0xf) << 4) + ((char_array_4[2] & 0x3c) >> 2);
    char_array_3[2] = ((char_array_4[2] & 0x3) << 6) + char_array_4[3];

    for (j = 0; (j < i - 1); j++) ret += char_array_3[j];
  }

  return ret;
}
/* end base64.cpp */

/* 
   base64.cpp and base64.h

   Copyright (C) 2004-2008 Ren Nyffenegger

   This source code is provided 'as-is', without any express or implied
   warranty. In no event will the author be held liable for any damages
   arising from the use of this software.

   Permission is granted to anyone to use this software for any purpose,
   including commercial applications, and to alter it and redistribute it
   freely, subject to the following restrictions:

   1. The origin of this source code must not be misrepresented; you must not
      claim that you wrote the original source code. If you use this source code
      in a product, an acknowledgment in the product documentation would be
      appreciated but is not required.

   2. Altered source versions must be plainly marked as such, and must not be
      misrepresented as being the original source code.

   3. This notice may not be removed or altered from any source distribution.

   Ren Nyffenegger rene.nyffenegger@adp-gmbh.ch

*/

/* http://ideone.com/nFVtEo */ // or http://stackoverflow.com/a/217605  in the toolbox until as an intrinsic language feature
string 
trim(string s) {

    string::const_iterator it = s.begin();
	
    while (it != s.end() && isspace(*it))
    it++;

    string::const_reverse_iterator rit = s.rbegin();
	
    while (rit.base() != it && isspace(*rit))
    rit++;

    return string(it, rit.base());
}

// split: receives a char delimiter; returns a vector of strings
// By default ignores repeated delimiters, unless argument rep == 1.
vector<string>& splitstring::split(char delim, unsigned int rep) {

	if (!flds.empty())
	flds.clear();  // empty vector if necessary
	
	string work = data();
    string buf = "";
    unsigned int i = 0;
    while (i < work.length()) {
	
        if (work[i] != delim)
            buf += work[i];
        else if (rep == 1) {
            flds.push_back(buf);
            buf = "";
        } else if (buf.length() > 0) {
            flds.push_back(buf);
            buf = "";
        }
        i++;
    }
	
    if (!buf.empty())
	flds.push_back(buf);
	
    return flds;
}

size_find
strpos ( string line, string sub, size_t start) {
	// note: do not change the return type of strpos to size_t because
	// -1 will be converted to some positive number

	if ( line.length() == 0 || start < 0 )
	return -1;

	if ( start > line.length() - 1 )
	return -1;
	
	size_t location = line.find( sub, start );
	
	if ( location == string::npos )
	return -1;

	return location; // implied else
}


string
squeeze( string s ) { // remove_space  // http://stackoverflow.com/a/83538

	string out = "";
	
	for(auto& it : s)
	if (!isspace(it))
	out += it;
	
	return out;
}
