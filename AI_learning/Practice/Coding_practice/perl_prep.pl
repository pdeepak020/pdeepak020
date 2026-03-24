# ============================================================
# Multithreading in Perl (using threads module)
# ============================================================
# Multithreading allows multiple parts of a program to run concurrently in the same process.
# You need to use the 'threads' module.
use threads;

# Example: Create two threads that print messages
sub thread_func {
    my $msg = shift;
    for (1..3) {
        print "Thread: $msg, Iteration: $_\n";
        sleep 1;
    }
}

my $thr1 = threads->create(\&thread_func, "A"); # Start thread A
my $thr2 = threads->create(\&thread_func, "B"); # Start thread B

$thr1->join(); # Wait for thread A to finish
$thr2->join(); # Wait for thread B to finish

# Explanation:
# - use threads; enables threading support.
# - thread_func is a subroutine that prints a message 3 times.
# - threads->create starts a new thread running thread_func with an argument.
# - join() waits for the thread to finish.

# ============================================================
# Multiprocessing in Perl (using fork)
# ============================================================
# Multiprocessing means running multiple processes, each with its own memory space.
# Perl uses fork() to create a child process.

my $pid = fork();
if (!defined $pid) {
    die "Fork failed!\n";
} elsif ($pid == 0) {
    # Child process
    for (1..3) {
        print "Child process: $_\n";
        sleep 1;
    }
    exit(0);
} else {
    # Parent process
    for (1..3) {
        print "Parent process: $_\n";
        sleep 1;
    }
    waitpid($pid, 0); # Wait for child to finish
}

# Explanation:
# - fork() creates a new process. Returns 0 in child, PID in parent.
# - Child and parent run their own loops and print messages.
# - waitpid waits for the child process to finish.

# ============================================================
# Difference: Multithreading vs Multiprocessing in Perl
# ============================================================
# Multithreading:
# - Threads share the same memory space.
# - Lightweight, easier to share data, but need to manage synchronization.
# - Example: use threads; my $thr = threads->create(\&func);
#
# Multiprocessing:
# - Each process has its own memory space.
# - Heavier, safer (no shared memory), but harder to share data.
# - Example: my $pid = fork(); if ($pid == 0) { ... }
#
# Example difference:
#
# # Threaded counter (shared variable)
# use threads;
# use threads::shared;
# my $counter :shared = 0;
# my $t = threads->create(sub { $counter++ for 1..5 });
# $t->join();
# print "Counter: $counter\n"; # Output: 5
#
# # Multiprocess counter (not shared)
# my $counter2 = 0;
# my $pid2 = fork();
# if ($pid2 == 0) { $counter2++ for 1..5; exit(0); }
# else { waitpid($pid2, 0); print "Counter: $counter2\n"; } # Output: 0
#
# In multiprocessing, changes in child do not affect parent variables.
#!/usr/bin/perl
# Reverse an array using a third variable
my @orig = (1, 2, 3, 4, 5);
my @rev = ();
for (my $i = $#orig; $i >= 0; $i--) {
    push @rev, $orig[$i];
}
print "Reversed with third variable: @rev\n"; # Output: 5 4 3 2 1

# Reverse an array in-place (without a third variable)
my @arr_inplace = (1, 2, 3, 4, 5);
my $n = scalar @arr_inplace;
for (my $i = 0; $i < int($n/2); $i++) {
    ($arr_inplace[$i], $arr_inplace[$n-$i-1]) = ($arr_inplace[$n-$i-1], $arr_inplace[$i]);
}
print "Reversed in-place: @arr_inplace\n"; # Output: 5 4 3 2 1
############################################################
# Perl Developer Preparation Notes
############################################################

# 1. Basic Perl Commands
#-----------------------
# Print statement
print "Hello, World!\n";

# Variable declaration
my $scalar = 10;
my @array = (1, 2, 3);
my %hash = ('a' => 1, 'b' => 2);

# Input from user
my $input = <STDIN>;
chomp($input);

# File operations
open(my $fh, '<', 'file.txt') or die $!;
#If open fails (e.g., file not found), $! will contain the reason, such as "No such file or directory".
#die $!; will print this error message and exit the program.
#Summary:
#$! gives you the error message for the most recent system call failure.

while (my $line = <$fh>) {
    print $line;
}
close($fh);

# Conditional statements
if ($scalar > 5) {
    print "Greater than 5\n";
} elsif ($scalar == 5) {
    print "Equal to 5\n";
} else {
    print "Less than 5\n";
}

# Loops
for my $i (0..4) {
    print "$i ";
}

foreach my $item (@array) {
    print "$item ";
}

while ($scalar > 0) {
    print "$scalar ";
    $scalar--;
}

# Subroutines
sub add {
    my ($a, $b) = @_;
    return $a + $b;
}
print add(2, 3);


############################################################
# Indexing and Slicing in Perl
############################################################
# Indexing: Accessing elements by position
my @nums = (10, 20, 30, 40, 50);
print $nums[0]; # Output: 10 (first element)
print $nums[-1]; # Output: 50 (last element)

# Slicing: Accessing multiple elements at once
my @slice = @nums[1, 3];
print "@slice\n"; # Output: 20 40

# String indexing
my $word = "hello";
print substr($word, 1, 3); # Output: ell (from index 1, length 3)

# Explanation:
# - Indexing uses square brackets for arrays, e.g., $arr[2]
# - Negative indices count from the end, e.g., $arr[-1] is last
# - Slicing uses a list of indices: @arr[1,3,4]
# - substr for string slicing: substr($str, start, length)

# Regular Expressions
my $str = "abc123";
if ($str =~ /\d+/) {
    print "Contains digits\n";
}

# More Regular Expression Examples for File Processing
# 1. Extract all email addresses from a file
open(my $fh_em, '<', 'emails.txt') or die $!;
while (my $line = <$fh_em>) {
    while ($line =~ /([\w.]+\@[\w.]+)/g) {
        print "Found email: $1\n";
    }
}
close($fh_em);

# 2. Replace all numbers with X in a file
open(my $fh_num, '<', 'numbers.txt') or die $!;
while (my $line = <$fh_num>) {
    $line =~ s/\d+/X/g;
    print $line;
}
close($fh_num);

# 3. Find lines starting with a specific word (e.g., 'Error')
open(my $fh_err, '<', 'log.txt') or die $!;
while (my $line = <$fh_err>) {
    print $line if $line =~ /^Error/;
}
close($fh_err);

# 4. Extract all words in double quotes
my $text = 'He said "hello" and then "bye".';
while ($text =~ /"([^"]+)"/g) {
    print "Quoted: $1\n";
}

# 2. OOP in Perl
#----------------
# Perl uses packages and bless for OOP
package Animal;
sub new {
    my ($class, $name) = @_;
    my $self = { name => $name };
    bless $self, $class;
    return $self;
}
sub speak {
    my $self = shift;
    print $self->{name} . " makes a sound\n";
}

package Dog;
our @ISA = qw(Animal); # Inheritance
sub speak {
    my $self = shift;
    print $self->{name} . " barks\n";
}

# Usage
my $dog = Dog->new("Rex");
$dog->speak();

# 3. Essential Perl Topics
#-------------------------
# - Scalars, Arrays, Hashes
# - Context (List vs Scalar)
# - References
my $ref_array = \@array;
my $ref_hash = \%hash;

# - Modules (use, require)
use strict;
use warnings;
use Data::Dumper;
print Dumper(\@array);

# - CPAN (Perl package manager)
# Install modules: cpan install Module::Name

# - Error handling
# die, warn, eval
open(my $fh2, '<', 'nofile.txt') or warn "File not found!\n";

# - Special variables
# $_, @_, $!, $?, $/ etc.

# - File and Directory operations
use File::Copy;
copy('file.txt', 'file_copy.txt');

use File::Path qw(make_path remove_tree);
make_path('new_dir');
remove_tree('new_dir');

# - System interaction
system('dir'); # Windows
system('ls');  # Unix

# - Command-line arguments
my $first_arg = $ARGV[0];

# - String manipulation
my $upper = uc($str);
my $lower = lc($str);
my $substr = substr($str, 0, 3);

# - Date and Time
use POSIX qw(strftime);
my $date = strftime "%Y-%m-%d", localtime;
print "$date\n";

# - Debugging
use Carp;
carp "This is a warning";

# - Testing
use Test::More tests => 1;
ok(1 == 1, 'One is one');

# 4. Useful Perl One-liners
#--------------------------
# perl -ne 'print if /pattern/' file.txt
# perl -pi -e 's/foo/bar/g' file.txt

# 5. Best Practices
#------------------
# - Always use 'strict' and 'warnings'
# - Use meaningful variable names
# - Comment your code
# - Use CPAN modules
# - Write tests
# - Handle errors gracefully

# 6. Resources
#-------------
# - https://perldoc.perl.org/
# - https://www.cpan.org/
# - https://learn.perl.org/
# - https://modernperlbooks.com/

############################################################
# End of Perl Developer Notes
############################################################

############################################################
# Additional Perl Concepts
############################################################

# 7. Database Interaction with DBI Module
#----------------------------------------
# DBI is the standard database interface for Perl
use DBI;
my $dsn = "DBI:mysql:database=testdb;host=localhost";
my $username = "root";
my $password = "password";
my $dbh = DBI->connect($dsn, $username, $password, { RaiseError => 1 }) or die $DBI::errstr;

# Simple SELECT query
my $sth = $dbh->prepare("SELECT * FROM users");
$sth->execute();
while (my @row = $sth->fetchrow_array()) {
    print join(", ", @row) . "\n";
}
$sth->finish();
$dbh->disconnect();

# 8. Using CPAN Modules
#----------------------
# CPAN is the Comprehensive Perl Archive Network for Perl modules
# To install a module from command line:
#   cpan install DBI
#   cpan install Data::Dumper

# Example: Using a CPAN module (Data::Dumper)
use Data::Dumper;
my @arr = (1, 2, 3);
print Dumper(\@arr);

# Example: Using a CPAN module (JSON)
use JSON;
my $json = encode_json({ name => "John", age => 30 });
print "$json\n";


# To update CPAN itself:
#   cpan CPAN

# To search for modules:
#   cpan search Module::Name

############################################################
# End of Additional Perl Concepts
############################################################

############################################################
# Common Perl Built-in Functions
############################################################

# 9. map
#--------
# Applies a block of code to each element in a list and returns a new list
my @squared = map { $_ * $_ } (1, 2, 3, 4);
print "@squared\n"; # Output: 1 4 9 16

# 10. grep
#----------
# Filters a list based on a condition
my @evens = grep { $_ % 2 == 0 } (1, 2, 3, 4, 5);
print "@evens\n"; # Output: 2 4

# 11. join
#----------
# Joins elements of a list into a single string with a separator
my $joined = join('-', 'a', 'b', 'c');
print "$joined\n"; # Output: a-b-c

# 12. split
#-----------
# Splits a string into a list using a pattern
my $text = "apple,banana,cherry";
my @fruits = split(/,/, $text);
print "@fruits\n"; # Output: apple banana cherry

# 13. sort
#----------
# Sorts a list
my @nums = (4, 2, 8, 1);
my @sorted = sort { $a <=> $b } @nums;
print "@sorted\n"; # Output: 1 2 4 8

#In Perl, the expression $a <=> $b is the "spaceship operator" for numeric comparison. It returns:

#-1 if $a is less than $b
#0 if $a is equal to $b
#1 if $a is greater than $b
#In the sort block:

#sort { $a <=> $b } @nums This tells Perl to sort @nums numerically in ascending order, comparing each pair of elements using their numeric values.
#If you used sort { $b <=> $a } @nums, it would sort in descending order

# 14. reverse
#-------------
# Reverses a list
my @reversed = reverse @nums;
print "@reversed\n"; # Output: 1 8 2 4

# 15. length
#------------
# Returns the length of a string
my $len = length("Hello");
print "$len\n"; # Output: 5

# 16. chomp
#-----------
# Removes the newline character from the end of a string
my $line = "Hello\n";
chomp($line);
print "$line\n"; # Output: Hello

# 17. push, pop, shift, unshift
#------------------------------
# Array operations
my @arr = (1, 2, 3);
push(@arr, 4);      # Add to end
my $last = pop(@arr);   # Remove from end
my $first = shift(@arr); # Remove from start
unshift(@arr, 0);    # Add to start
print "@arr\n"; # Output: 0 2 3

# 18. keys, values, each
#-----------------------
# Hash operations
my %h = (a => 1, b => 2);
my @keys = keys %h;
my @vals = values %h;
while (my ($k, $v) = each %h) {
    print "$k => $v\n";
}

# 19. defined, undef
#-------------------
my $x;
print defined($x) ? "Defined\n" : "Undefined\n";
$x = 10;
undef $x;
print defined($x) ? "Defined\n" : "Undefined\n";

# 20. die, warn
#--------------
die "Fatal error!\n" if 0;
warn "This is a warning\n";

############################################################
# End of Perl Built-in Functions
############################################################

############################################################
# Advanced Perl Interview Concepts
############################################################

# 21. References and Complex Data Structures
#-------------------------------------------
# Array of arrays
my @matrix = ([1, 2], [3, 4]);
print $matrix[0]->[1]; # Output: 2

# Hash of hashes
my %users = (
    alice => { age => 30, city => 'NY' },
    bob   => { age => 25, city => 'LA' }
);
print $users{alice}{city}; # Output: NY

# 22. Anonymous Subroutines (Closures)
#-------------------------------------
my $adder = sub {
    my ($x, $y) = @_;
    return $x + $y;
};
print $adder->(2, 3); # Output: 5

# 23. AUTOLOAD and Symbol Table Manipulation
#-------------------------------------------
package Dynamic;
sub AUTOLOAD {
    our $AUTOLOAD;
    print "Called $AUTOLOAD\n";
}
my $obj = bless {}, 'Dynamic';
$obj->foo(); # Calls AUTOLOAD

# 24. Tied Variables
#-------------------
# Custom behavior for variables
package MyArray;
use Tie::Array;
our @ISA = ('Tie::Array');
sub FETCH {
    my ($self, $idx) = @_;
    return "Value $idx";
}
tie my @arr, 'MyArray';
print $arr[2]; # Output: Value 2

# 25. Perl XS (C Extensions)
#--------------------------
# XS allows writing Perl modules in C for performance
# (Usually asked conceptually, not for code)
# See: https://perldoc.perl.org/perlxs

# 26. Moose/Moo (Modern OOP Frameworks)
#--------------------------------------
# Moose and Moo provide advanced OOP features
# Example:
# use Moose;
# has 'name' => (is => 'rw', isa => 'Str');
# my $obj = MyClass->new(name => 'John');

# 27. Regular Expression Advanced Features
#----------------------------------------
# Non-greedy match
my $txt = 'abc123def456';
$txt =~ /(\d+?)/;
print $1; # Output: 1

# Named capture
$txt =~ /(?<digits>\d+)/;
print $+{digits};

# 28. Perl One-liners and Command-line Tricks
#--------------------------------------------
# perl -E 'say for 1..5'
# perl -lne 'print if /error/' logfile.txt

# 29. Memory Management and Optimization
#--------------------------------------
# Use references for large data
# Avoid unnecessary copies
# Use modules like Devel::Size, Devel::Peek for inspection

# 30. Exception Handling with Try::Tiny
#--------------------------------------
use Try::Tiny;
try {
    die "Oops!";
} catch {
    warn "Caught error: $_";
};

############################################################
# End of Advanced Perl Interview Concepts
############################################################

############################################################
# DSA (Data Structures & Algorithms) Perl Questions/Examples
############################################################

# 1. Fibonacci Sequence (Recursion)
sub fib {
    my ($n) = @_;
    return $n if $n < 2;
    return fib($n-1) + fib($n-2);
}
print fib(6); # Output: 8

# 2. Reverse a String
my $str1 = "hello";
my $rev = reverse $str1;
print $rev; # Output: olleh

# 3. Check Palindrome
sub is_palindrome {
    my ($s) = @_;
    return $s eq reverse $s;
}
print is_palindrome("level") ? "Palindrome\n" : "Not palindrome\n";

# 4. Check Anagram
sub is_anagram {
    my ($a, $b) = @_;
    return join('', sort split('', $a)) eq join('', sort split('', $b));
}
print is_anagram("listen", "silent") ? "Anagram\n" : "Not anagram\n";

# 5. Concatenate Two Strings
my $a = "foo";
my $b = "bar";
my $c = $a . $b;
print $c; # Output: foobar

# 6. Recursion Example: Factorial
sub fact {
    my ($n) = @_;
    return 1 if $n <= 1;
    return $n * fact($n-1);
}
print fact(5); # Output: 120

# 7. Reverse an Array
my @arr = (1,2,3,4);
my @rev_arr = reverse @arr;
print "@rev_arr\n"; # Output: 4 3 2 1

# 8. Find Maximum in Array
my $max = $arr[0];
foreach my $v (@arr) {
    $max = $v if $v > $max;
}
print "Max: $max\n";

# 9. Merge Two Arrays
my @a1 = (1,2);
my @a2 = (3,4);
my @merged = (@a1, @a2);
print "@merged\n"; # Output: 1 2 3 4

# 10. Count Occurrences of Each Character
my $word2 = "banana";
my %count;
$count{$_}++ for split('', $word2);
foreach my $k (keys %count) {
    print "$k: $count{$k}\n";
}

# These are common DSA-style questions in Perl for interviews and practice.

# Difference between 'require' and 'use' in Perl
# ==============================================
#
# 'require':
# - Loads a module or file at runtime (when the statement is executed).
# - Does not automatically import symbols (functions/variables) into your namespace.
# - Typically used for conditional or dynamic loading.
# - Example:
#   require MyModule;
#   MyModule::function();
#
# 'use':
# - Loads a module at compile time (before your script runs).
# - Automatically calls the module's import() method, importing symbols into your namespace (unless you specify otherwise).
# - Commonly used for standard modules and pragma.
# - Example:
#   use MyModule;
#   function();  # if exported by MyModule
#
# Summary:
# - 'use' is for compile-time loading and symbol importing.
# - 'require' is for runtime loading, no automatic import.
# - Both are used to include modules, but 'use' is preferred for most cases.
