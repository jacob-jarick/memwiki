Quick dump for doing audits.


This isnt worth others reading yet.

# Tennants

## List

display all tennants

```
Get-AzTenant | Select-Object Id, DisplayName, Country, Domains
```

## Swap

I work out of windows terminal, love it.

problem, when swapping tennants you cant use the default command

solution

use  -UseDeviceAuthentication option

```
Connect-AzAccount -TenantId "c87e0a28-0665-4f48-bf3b-XXXXXXXXX" -UseDeviceAuthentication
```
