# Formatting Export Certificate Reference Numbers Script for Docbits

This document outlines the "Formatting Export Certificate Reference Numbers" script, aimed at standardizing reference numbers across export certificates in Docbits. Proper formatting ensures that reference numbers comply with external systems or regulatory requirements.

### Purpose

The script's primary goal is to format reference numbers on export certificates, ensuring they meet a predefined length requirement by padding them with leading zeros. This consistency aids in maintaining a standardized format for all export documents processed through Docbits.

### Script Overview

The script identifies the `reference_number` field in an export certificate, checks its length, and if necessary, pads the number with leading zeros to ensure it meets the minimum length requirement.

#### Code Snippet

```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Ensure the reference number meets a minimum length of 10 characters
if len(ref_number) < 10:
    ref_number = ref_number.zfill(10)
    set_field_value(fields_dict, 'reference_number', ref_number)
```


