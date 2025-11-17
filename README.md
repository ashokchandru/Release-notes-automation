In the future most technical documentation will be in JSON. But, for the time being we will use Markdown for documentation.
We will use JSON to give inputs to the LLM to create strrcutured consistent output.

Historic release notes are stored in repository

Full automation: (Doesn't work for organizations w)
Agent looks for Git commits and Pull requests when you add a tag e.g. RN, it the content is copied for release notes
### Reasons why this is impractical: 
* The product team should curate which features or tickets to be shown in the release notes
* It will be difficult to edit already generated release notes

# Best practical approach:
* Technical Writer collects the content, "New Features", "Known Issues", "Fixed Issues" based on the release notes format
* Creates the source of truth in JSON file with the change data (updates.json). (You can also use yaml, but the indentation issues is an unnecessary headache. Go for JSON for better structure)
* Uploads the JSON file to the agent
~~~
# Reasons to choose JSON over prompt engineering
* LLMs are not robust enough to produce strcutured content based on prompts.
* Future of prompt engineering is going to be JSON or YAML.
* JSON format is great for the agent to interact with LLMs.~~~
~~~
* Agent reads the JSON file
* Agent creates the new release notes in the format of an md file
* Posts the file to a review folder in the repository
* Agent opens a pull request
* Technical writer reviews the pull request and commits the changes
* Final version approved by the writer or PM

Agent side work: 
* Create either local or web agent
* Mapping is defined in agent code
* Check input.json file in repository
* new_feature from JSON mapped to "New Features"
* konwn_issues from JSON mapped to "Known Issues"
