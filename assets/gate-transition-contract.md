# Gate Transition Contract

This is the deterministic contract behind the natural-language workflow.

| Event | Required state | Result |
|---|---|---|
| Display task card `TC-N` | Any | Gate A becomes Pending(`TC-N`); downstream artifacts are invalidated if content changed. |
| Confirm task card `TC-N` | Gate A Pending(`TC-N`) and card was displayed | Gate A becomes Passed(`TC-N`); research may start. |
| Modify or supplement task card | Any pending/passed task card | Create and display `TC-(N+1)`; Gate A stays Pending; old confirmation is invalid. |
| Display review package `RP-N` | Gate A Passed for current task card | Gate B becomes Pending(`RP-N`). |
| Select/delegate `RP-N` | Gate B Pending(`RP-N`) and RP-N was displayed before the response | Gate B becomes Passed(`RP-N`); validation/package/implementation may start subject to risk policy. |
| Materially revise research or review package | Any review state | Create and display `RP-(N+1)`; Gate B becomes Pending; old selection is invalid. |
| Try to validate or implement | Both current gates passed and no gray blocker | Allowed; otherwise stop and show the missing gate. |

Version evidence must include the displayed artifact reference and the user response reference. A statement made before an artifact version is displayed cannot approve that version.
