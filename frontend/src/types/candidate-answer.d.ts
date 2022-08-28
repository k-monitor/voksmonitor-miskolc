/* tslint:disable */
/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */

/**
 * A representation of answers for given candidate to questions
 */
export interface CandidateAnswer {
  /**
   * UUID
   */
  id: string;
  /**
   * Candidate's UUID
   */
  candidate_id: string;
  /**
   * Question's UUID
   */
  question_id: string;
  /**
   * Answer on given question
   */
  answer?: 'yes' | 'no';
  /**
   * Candidate's comment related to their answer.
   */
  comment?: string;
  [k: string]: unknown;
}
