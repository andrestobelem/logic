# Domain discovery

The domain is not defined yet. The repository name does not define the domain.
This document is the source for the domain model and its terms.

## Purpose

Not defined. Agree on the problem and the expected result before you add domain
behavior.

## Actors

No actors are defined. Record who uses the system and what each actor needs.

## Use cases

No use cases are defined. For each use case, record the actor, goal, inputs,
expected result, and failure conditions.

## Terms

No domain terms are agreed yet. Use the following table when a term is agreed.
Add rows only for agreed concepts. A synonym to avoid is an alternative name
that must not replace the agreed term in its context.

| Term in English | Context | Definition | Examples | Rules | Synonyms to avoid |
| --- | --- | --- | --- | --- | --- |

Use the same terms in code, APIs, tests, and documentation. Use technical names
as permitted by ASD-STE100. Check other words against its approved dictionary.
If a term has different meanings, record a separate definition for each context.

## Rules and examples

No domain rules are agreed yet. For each rule, record:

1. The condition that applies.
2. The expected behavior.
3. A valid example and its result.
4. An invalid or boundary example and its result, when applicable.

Turn the agreed examples into tests before you implement the behavior. Test
observable results rather than internal code structure.

## Model decisions

No entities, value objects, or context boundaries are defined. Add them when
the rules require them. Record the reason for each decision.

Keep definitions, code, and tests consistent when a concept changes. Update
them in the same change.

## Open questions

- What problem must `logic` solve?
- Who needs the result?
- Which use case must the system support first?
- Which examples show a correct result and an incorrect result?
- Which rules must always hold?

## Discovery steps

1. Agree on the purpose and actors.
2. Select one use case and collect concrete examples.
3. Agree on the terms and observable rules. Record questions that remain open.
4. Write tests for the agreed examples.
5. Implement the smallest model that satisfies the rules.
6. Review the model and terms with new evidence.
