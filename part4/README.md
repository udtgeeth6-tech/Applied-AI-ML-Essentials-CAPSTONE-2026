**Track a pipeline testing**
The complete track a pipeline was tested on three distinct inputs. Before each LLM call, a regex-based guardrail checked the input personally identifiable information (pII), including email addresses and phone numbers. Inputs containing PII were blocked and not sent to the LLM. For inputs that passed the guardrail, the LLM generated structured JSON output, which was parsed using json.load() and validated againt the predefined schema using jsonschema.validate(). The first two inputs successfully produced valid JSON matching the schema, while the third input was blocked because it contained an email address.
**Temperature setting for extraction**
Temperature was set to 0 for the primary extraction pipeline because structured Json extraction requires deterministic and reproducible outputs. At temperature = 0, the model consistently selects the highest – probability next token, reducing randomness and improving the likelihood that the generated output conforms to the expected schema. In contrast, temperature = 0.7 introduces sampling from a boarder probability distribution, which can produce more varied wording and occasionally alter the JSON structure. Therefore, temperature = 0 is preferred for structured data extraction and validation tasks
**
Guardrail implementation**
A regex-based guardrail was implemented before every LLM call to detect personally identifiable information(PII). The guardrail checks for email addresses and phone numbers using regular expressions. If PII is detected, the request is blocked, the message “input blocked”: PII detected.” Is printed, and the LLM is not called. Two test cases were executed: one containing an email address, which was successfully blocked, and one containing only laptop specifications, which proceeded normally to the LLM. This guardrail helps prevent accidental transmission of sensitive personal information to external LLM services.
**Pipeline testing results**
The pipeline was tested on three different input texts. The first two inputs contained all the information required by the extraction schema, allowing the LLM to generate valid JSON that was successfully parsed using Json.loads() and validating using  jsonschema.validate(). The third input contained only a general description and lacked several required fields, causing the model output to fail schema validation. The observed pattern was the inputs containing explicts values for all required attributes (company, CPU, RAM, storage, and price category) were more likely to produce valid structured JSON, while incomplete or ambiguous inputs resulted in missing fields or invalid outputs. 
**LLM Response handling**
After each LLM call, the response text was cleaned using response.strip() to remove leading and trailing whitespace. The cleaned response was parsed into a python dictionary using json.loads() inside a try-expert json.JSONDecodeError block. The parsed dictionary was then validated against the predefined JSON schema using Jsonschema.validate(). Validation was performed inside a try-expect validationError block. If either JSON parsing or schema validation failed, an error message was printed and a fallback value(None or a dictionary with null fields) was returned. This approach ensures robust handling of malformed or unexpected model outputs.







