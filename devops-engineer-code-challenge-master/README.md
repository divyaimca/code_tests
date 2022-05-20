# Devops Engineer Code Challenge

Email the candidate the following instructions and the sample.log.zip

## Getting Started

Here's a [compressed log file](sample.log.zip). Extract it and have a quick look at the format.

Now, write a command line tool that parses the log and presents the following info to the user:

- What are the number of requests served by day?
- What are the 3 most frequent User Agents by day?
- What is the ratio of GET's to POST's by OS by day?

## Guidelines

Use the following tools:

- GitHub
- Java or Python
- Your favorite editor

Organize the project as you would normally structure a production-ready tool.

## Ship it

Once you’re done, send us a link to your GitHub repo. We’ll review based on:

- Code quality
- Best­ practices
- Testing
- Design
- Style

## Bonus Points

- Add command line switches (e.g., verbose mode)
- Provide a help screen
- Provide sufficient test coverage

## Usage Help
python3 log_parser.py --help

e.g. python3 log_parser.py --logFile sample.log  --date 01/Dec/2011 --action all

## Testing

python3 test_coverage.py


