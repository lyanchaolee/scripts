package com.alibaba.test;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.LineNumberReader;

public class RunDNASortingTest {

    private static final String BLANK                = " ";

    private static final String TEN_SIX_CASE         = "AACATGAAGG TTTTGGCCAA TTTGGCCAAA GATCAGATTT CCCGGGGGGA ATCGATGCAT";
    private static final String TEN_SIX_RESULT       = "TEST1 TEST2";

    private static final String TWENTY_FIFTY_CASE    = "AACATGAAGG TTTTGGCCAA TTTGGCCAAA GATCAGATTT CCCGGGGGGA ATCGATGCAT";
    private static final String TWENTY_FIFTY_RESULT  = "TEST1 TEST2";

    private static final String FIFTY_HUNDRED_CASE   = "AACATGAAGG TTTTGGCCAA TTTGGCCAAA GATCAGATTT CCCGGGGGGA ATCGATGCAT";
    private static final String FIFTY_HUNDRED_RESULT = "TEST1 TEST2";

    public static void main(String[] args) throws IOException, InterruptedException {
        if (args == null || (args.length != 2 && args.length != 4)) {
            throw new IllegalArgumentException("argument error");
        }

        if ("java".equals(args[0])) {
            callAndMeasure("java -classpath " + args[2], args[3]);
        } else if ("shell".equals(args[0])) {
            callAndMeasure("/bin/sh", args[1]);
        } else if ("python".equals(args[0])) {
            callAndMeasure("python", args[1]);
        }

    }

    private static void callAndMeasure(String programCommand, String programName) throws IOException,
                                                                                 InterruptedException {
        String tenSixResult = exe(programCommand, programName, TEN_SIX_CASE);
        checkResult(TEN_SIX_CASE, tenSixResult, TEN_SIX_RESULT);
        String twentyFiftyResult = exe(programCommand, programName, TWENTY_FIFTY_CASE);
        checkResult(TWENTY_FIFTY_CASE, twentyFiftyResult, TWENTY_FIFTY_RESULT);

        long timeBegin = System.currentTimeMillis();
        String fiftyHundredResult = exe(programCommand, programName, FIFTY_HUNDRED_CASE);
        checkResult(FIFTY_HUNDRED_CASE, fiftyHundredResult, FIFTY_HUNDRED_RESULT);
        System.out.println("sucess and cost in mili seconds: " + (System.currentTimeMillis() - timeBegin));
    }

    private static void checkResult(String input, String tenSixResult, String tenSixResult2) {
        if (tenSixResult.trim().equals(tenSixResult2.trim())) {

        } else {
            throw new RuntimeException("result not right in the case of : " + input + " , the result is: "
                                       + tenSixResult);
        }

    }

    private static String exe(String programType, String programName, String parameters) throws IOException,
                                                                                        InterruptedException {
        Process process = Runtime.getRuntime().exec(programType + BLANK + programName + BLANK + parameters);

        process.waitFor();

        InputStreamReader irError = new InputStreamReader(process.getErrorStream());
        LineNumberReader errorStreamReader = new LineNumberReader(irError);
        StringBuilder resultErrorBuilder = new StringBuilder();
        String resultError;
        while ((resultError = errorStreamReader.readLine()) != null) {
            resultErrorBuilder.append(resultError);
        }

        if (resultErrorBuilder.toString() != null && !resultErrorBuilder.toString().isEmpty()) {
            throw new RuntimeException(resultErrorBuilder.toString());
        }
        InputStreamReader ir = new InputStreamReader(process.getInputStream());
        LineNumberReader infoStreamReader = new LineNumberReader(ir);
        StringBuilder resultInfoBuilder = new StringBuilder();
        String resultInfo;
        while ((resultInfo = infoStreamReader.readLine()) != null) {
            resultInfoBuilder.append(resultInfo.trim()).append(BLANK);
        }

        return resultInfoBuilder.toString();
    }
}
